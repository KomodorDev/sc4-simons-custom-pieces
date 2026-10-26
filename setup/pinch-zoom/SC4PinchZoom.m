#import <Cocoa/Cocoa.h>
#include <crt_externs.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// No system event tap or input-posting permission is used. Events stay in NSApp.
static const double kPinchThreshold = 0.12;
static const double kGestureGap = 0.6;

typedef struct {
    double accumulated;
    double lastTime;
    bool hasEvent;
    bool fired;
    bool phased;
} PinchState;

static void ResetPinch(PinchState *state) {
    memset(state, 0, sizeof(*state));
}

static int AdvancePinch(PinchState *state, double amount, double timestamp,
                        bool began, bool ended, bool cancelled, bool hasPhase) {
    if (cancelled || !isfinite(amount) || !isfinite(timestamp)) {
        ResetPinch(state);
        return 0;
    }
    if (began || (state->hasEvent &&
                  (timestamp < state->lastTime ||
                   (!state->phased && !hasPhase && timestamp - state->lastTime > kGestureGap)))) {
        ResetPinch(state);
    }
    state->phased = state->phased || hasPhase;
    state->hasEvent = true;
    state->lastTime = timestamp;
    int step = 0;
    if (!state->fired) {
        state->accumulated += amount;
        if (state->accumulated >= kPinchThreshold) step = 1;
        else if (state->accumulated <= -kPinchThreshold) step = -1;
        if (step) state->fired = true;
    }
    if (ended) ResetPinch(state);
    return step;
}

static bool IsGameArgument(const char *argument) {
    if (!argument) return false;
    const char *name = argument;
    for (const char *p = argument; *p; ++p) {
        if (*p == '/' || *p == '\\') name = p + 1;
    }
    return strcasecmp(name, "SimCity 4.exe") == 0;
}

static bool HasGameArgument(int count, char *const *arguments) {
    for (int i = 0; i < count; ++i) {
        if (IsGameArgument(arguments[i])) return true;
    }
    return false;
}

static NSEvent *ZoomKeyEvent(NSEventType type, int direction, NSInteger windowNumber,
                             NSPoint location, NSTimeInterval timestamp,
                             NSEventModifierFlags modifiers) {
    NSString *characters = direction > 0 ? @"+" : @"-";
    return [NSEvent keyEventWithType:type
                           location:location
                      modifierFlags:modifiers | NSEventModifierFlagNumericPad
                          timestamp:timestamp
                       windowNumber:windowNumber
                            context:nil
                         characters:characters
        charactersIgnoringModifiers:characters
                          isARepeat:NO
                            keyCode:direction > 0 ? 69 : 78];
}

#ifndef SC4_PINCH_TEST

static PinchState pinch;
static id eventMonitor;
static id focusObserver;
static id terminationObserver;
static NSString *statusPath;
static NSString *bridgeState = @"waiting_for_wine";
static uint64_t magnifyEvents, zoomInSteps, zoomOutSteps, ignoredMagnifyEvents, focusResets;
static NSInteger targetWindowNumber;
static double lastStatusTime;

static void Increment(uint64_t *counter) {
    if (*counter < UINT64_MAX) ++*counter;
}

static void WriteStatus(BOOL force) {
    if (!statusPath) return;
    double now = NSProcessInfo.processInfo.systemUptime;
    if (!force && now - lastStatusTime < 0.25) return;
    lastStatusTime = now;
    // Only this bridge's state and counters are recorded, never keys or window text.
    NSDictionary *status = @{
        @"schema": @1, @"pid": @(getpid()), @"state": bridgeState,
        @"magnify_events": @(magnifyEvents), @"zoom_in_steps": @(zoomInSteps),
        @"zoom_out_steps": @(zoomOutSteps), @"ignored_magnify_events": @(ignoredMagnifyEvents),
        @"focus_resets": @(focusResets), @"threshold": @(kPinchThreshold),
        @"updated_unix_seconds": @([NSDate date].timeIntervalSince1970)
    };
    NSData *data = [NSJSONSerialization dataWithJSONObject:status options:0 error:NULL];
    if (data) [data writeToFile:statusPath options:NSDataWritingAtomic error:NULL];
}

static BOOL EligibleWindow(NSEvent *event) {
    NSWindow *window = event.window;
    Class wineWindow = NSClassFromString(@"WineWindow");
    NSEventModifierFlags excluded = NSEventModifierFlagCommand | NSEventModifierFlagShift |
                                   NSEventModifierFlagControl | NSEventModifierFlagOption;
    return NSApp.isActive && window && window == NSApp.keyWindow && wineWindow &&
           [window isKindOfClass:wineWindow] &&
           [window.title caseInsensitiveCompare:@"SimCity 4"] == NSOrderedSame &&
           !(event.modifierFlags & excluded);
}

static NSEvent *HandleGesture(NSEvent *event) {
    if (event.type != NSEventTypeMagnify) {
        // Preserve all generic gesture markers; other gestures remain untouched.
        BOOL hadMagnification = pinch.hasEvent;
        ResetPinch(&pinch);
        if (hadMagnification && event.type == NSEventTypeEndGesture) WriteStatus(YES);
        return event;
    }
    Increment(&magnifyEvents);
    if (!EligibleWindow(event)) {
        ResetPinch(&pinch);
        targetWindowNumber = 0;
        Increment(&ignoredMagnifyEvents);
        WriteStatus(NO);
        return event;
    }
    if (targetWindowNumber != event.windowNumber) {
        ResetPinch(&pinch);
        targetWindowNumber = event.windowNumber;
    }
    NSEventPhase phase = event.phase;
    int step = AdvancePinch(&pinch, event.magnification, event.timestamp,
                            (phase & NSEventPhaseBegan) != 0,
                            (phase & NSEventPhaseEnded) != 0,
                            (phase & NSEventPhaseCancelled) != 0,
                            phase != NSEventPhaseNone);
    if (step) {
        NSEvent *down = ZoomKeyEvent(NSEventTypeKeyDown, step, event.windowNumber,
                                     event.locationInWindow, event.timestamp, event.modifierFlags);
        NSEvent *up = ZoomKeyEvent(NSEventTypeKeyUp, step, event.windowNumber,
                                   event.locationInWindow, event.timestamp, event.modifierFlags);
        if (down && up) {
            // A fresh dispatch must pass through WineApplication's input handler.
            [NSApp postEvent:down atStart:NO];
            [NSApp postEvent:up atStart:NO];
            Increment(step > 0 ? &zoomInSteps : &zoomOutSteps);
        }
    }
    WriteStatus(step != 0 || (phase & (NSEventPhaseEnded | NSEventPhaseCancelled)) != 0);
    return nil;
}

static void InstallWhenWineIsReady(unsigned attempt) {
    @autoreleasepool {
        Class wineApplication = NSClassFromString(@"WineApplication");
        if (!NSApp || !wineApplication || ![NSApp isKindOfClass:wineApplication] ||
            ![NSApp respondsToSelector:NSSelectorFromString(@"setWineController:")]) {
            if (attempt >= 240) {
                bridgeState = @"wine_not_ready";
                WriteStatus(YES);
                return;
            }
            dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 250 * NSEC_PER_MSEC),
                           dispatch_get_main_queue(), ^{ InstallWhenWineIsReady(attempt + 1); });
            return;
        }
        if (eventMonitor) return;
        eventMonitor = [NSEvent addLocalMonitorForEventsMatchingMask:
            NSEventMaskMagnify | NSEventMaskBeginGesture | NSEventMaskEndGesture
            handler:^NSEvent *(NSEvent *event) { return HandleGesture(event); }];
        if (!eventMonitor) {
            bridgeState = @"monitor_unavailable";
            WriteStatus(YES);
            return;
        }
        focusObserver = [[NSNotificationCenter defaultCenter]
            addObserverForName:NSApplicationDidResignActiveNotification object:NSApp
            queue:[NSOperationQueue mainQueue] usingBlock:^(NSNotification *notification) {
                (void)notification;
                ResetPinch(&pinch);
                targetWindowNumber = 0;
                Increment(&focusResets);
                WriteStatus(YES);
            }];
        terminationObserver = [[NSNotificationCenter defaultCenter]
            addObserverForName:NSApplicationWillTerminateNotification object:NSApp
            queue:[NSOperationQueue mainQueue] usingBlock:^(NSNotification *notification) {
                (void)notification;
                if (eventMonitor) [NSEvent removeMonitor:eventMonitor];
                eventMonitor = nil;
                if (focusObserver) [[NSNotificationCenter defaultCenter] removeObserver:focusObserver];
                focusObserver = nil;
                ResetPinch(&pinch);
                bridgeState = @"stopped";
                WriteStatus(YES);
            }];
        bridgeState = @"monitor_installed";
        WriteStatus(YES);
    }
}

__attribute__((constructor)) static void SC4PinchStart(void) {
    // Check C argv/environment before sending any Objective-C messages.
    const char *enabled = getenv("SC4_PINCH_ENABLED");
    if (!enabled || strcmp(enabled, "1") != 0 ||
        !HasGameArgument(*_NSGetArgc(), *_NSGetArgv())) return;
    const char *rawPath = getenv("SC4_PINCH_STATUS");
    char *pathCopy = rawPath ? strdup(rawPath) : NULL;
    dispatch_async(dispatch_get_main_queue(), ^{
        @autoreleasepool {
            if (pathCopy) {
                NSString *candidate = [[NSString alloc] initWithUTF8String:pathCopy];
                if (candidate.isAbsolutePath) statusPath = candidate;
                free(pathCopy);
            }
            WriteStatus(YES);
            // Never call sharedApplication: Wine must create its own subclass first.
            InstallWhenWineIsReady(0);
        }
    });
}

#else

#include <assert.h>
#include <stdio.h>

int main(void) {
    PinchState state = {0};
    assert(AdvancePinch(&state, 0.04, 1.0, true, false, false, true) == 0);
    assert(AdvancePinch(&state, 0.09, 1.1, false, false, false, true) == 1);
    assert(AdvancePinch(&state, 0.50, 1.2, false, false, false, true) == 0);
    assert(AdvancePinch(&state, -0.50, 1.3, false, false, false, true) == 0);
    assert(AdvancePinch(&state, 0, 1.4, false, true, false, true) == 0);
    assert(AdvancePinch(&state, -0.13, 1.5, true, false, false, true) == -1);
    assert(AdvancePinch(&state, 0.13, 2.2, false, false, false, true) == 0); // a paused phased pinch still fires only once
    ResetPinch(&state);
    assert(AdvancePinch(&state, 0.13, 2.3, false, false, false, false) == 1);
    assert(AdvancePinch(&state, -0.13, 3.0, false, false, false, false) == -1); // phase-less stream timeout
    ResetPinch(&state); // focus loss or a generic gesture boundary
    assert(AdvancePinch(&state, -0.07, 3.1, false, false, false, false) == 0);
    ResetPinch(&state);
    assert(AdvancePinch(&state, -0.07, 3.2, false, false, false, false) == 0);
    assert(AdvancePinch(&state, -0.13, 3.3, false, false, true, true) == 0);
    assert(AdvancePinch(&state, 0.13, 3.4, true, true, false, true) == 1);
    assert(AdvancePinch(&state, -0.13, 3.5, true, false, false, true) == -1);
    assert(AdvancePinch(&state, NAN, 3.6, false, false, false, true) == 0);
    assert(IsGameArgument("SimCity 4.exe"));
    assert(IsGameArgument("C:\\Games\\SimCity 4.exe"));
    assert(IsGameArgument("/game/SimCity 4.exe"));
    assert(!IsGameArgument("echo SimCity 4.exe"));
    assert(!IsGameArgument("SimCity 4.exe.bak"));
    char *args[] = {"wine32on64", "C:\\Games\\SimCity 4.exe", "-w"};
    assert(HasGameArgument(3, args));
    @autoreleasepool {
        assert(NSApp == nil);
        for (int direction = -1; direction <= 1; direction += 2) {
            for (int release = 0; release <= 1; ++release) {
                NSEventType type = release ? NSEventTypeKeyUp : NSEventTypeKeyDown;
                NSEvent *event = ZoomKeyEvent(type, direction, 0, NSMakePoint(12, 34), 7.5, 0);
                assert(event && event.type == type);
                assert(event.keyCode == (direction > 0 ? 69 : 78));
                assert([event.characters isEqualToString:direction > 0 ? @"+" : @"-"]);
                assert([event.charactersIgnoringModifiers isEqualToString:event.characters]);
                assert((event.modifierFlags & NSEventModifierFlagNumericPad) != 0);
                assert(event.windowNumber == 0 && event.timestamp == 7.5);
                assert(NSEqualPoints(event.locationInWindow, NSMakePoint(12, 34)));
                assert(!event.isARepeat);
            }
        }
        assert(NSApp == nil);
    }
    puts("PASS: pinch state, process arguments, and keypad events; no NSApp created or events posted.");
    return 0;
}

#endif
