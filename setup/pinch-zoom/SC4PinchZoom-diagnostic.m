#import <Cocoa/Cocoa.h>
#include <crt_externs.h>
#include <errno.h>
#include <fcntl.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/sysctl.h>
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
static CFRunLoopTimerRef readinessTimer;
static unsigned readinessAttempts;

static bool KernelArgumentsMatch(bool *querySucceeded) {
    *querySucceeded = false;
    int mib[] = {CTL_KERN, KERN_PROCARGS2, getpid()};
    size_t length = 0;
    if (sysctl(mib, 3, NULL, &length, NULL, 0) != 0 ||
        length <= sizeof(int) || length > 2 * 1024 * 1024) return false;
    char *data = malloc(length);
    if (!data) return false;
    if (sysctl(mib, 3, data, &length, NULL, 0) != 0 || length <= sizeof(int)) {
        free(data);
        return false;
    }
    int count;
    memcpy(&count, data, sizeof(count));
    char *end = data + length;
    char *cursor = memchr(data + sizeof(int), '\0', length - sizeof(int));
    bool matched = false;
    if (!cursor || count < 0 || count > 65536) {
        free(data);
        return false;
    }
    // Skip the executable path and its padding, then examine argc arguments only.
    ++cursor;
    while (cursor < end && !*cursor) ++cursor;
    for (int i = 0; i < count; ++i) {
        char *terminator = memchr(cursor, '\0', (size_t)(end - cursor));
        if (!terminator) {
            free(data);
            return false;
        }
        if (IsGameArgument(cursor)) matched = true;
        cursor = terminator + 1;
    }
    *querySucceeded = true;
    free(data);
    return matched;
}

static void WriteBootstrap(const char *path, int argumentCount, bool crtMatch,
                           bool kernelMatch, bool kernelQuerySucceeded) {
    if (!path || path[0] != '/' || strlen(path) > 3500) return;
    char output[4096], temporary[4096], json[512];
    int n = snprintf(output, sizeof(output), "%s.bootstrap.%ld.json", path, (long)getpid());
    if (n < 0 || (size_t)n >= sizeof(output)) return;
    n = snprintf(temporary, sizeof(temporary), "%s.XXXXXX", output);
    if (n < 0 || (size_t)n >= sizeof(temporary)) return;
    n = snprintf(json, sizeof(json),
        "{\"schema\":1,\"pid\":%ld,\"state\":\"constructor_entered\","
        "\"enabled\":true,\"crt_argc\":%d,\"crt_argument_match\":%s,"
        "\"kernel_query_succeeded\":%s,\"kernel_argument_match\":%s,\"accepted\":%s}\n",
        (long)getpid(), argumentCount, crtMatch ? "true" : "false",
        kernelQuerySucceeded ? "true" : "false", kernelMatch ? "true" : "false",
        (crtMatch || kernelMatch) ? "true" : "false");
    if (n < 0 || (size_t)n >= sizeof(json)) return;
    int fd = mkstemp(temporary);
    if (fd < 0) return;
    size_t written = 0;
    while (written < (size_t)n) {
        ssize_t count = write(fd, json + written, (size_t)n - written);
        if (count < 0 && errno == EINTR) continue;
        if (count <= 0) break;
        written += (size_t)count;
    }
    bool complete = written == (size_t)n;
    if (close(fd) != 0) complete = false;
    if (!complete || rename(temporary, output) != 0) unlink(temporary);
}

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

static BOOL InstallWhenWineIsReady(void) {
    @autoreleasepool {
        Class wineApplication = NSClassFromString(@"WineApplication");
        if (!NSApp || !wineApplication || ![NSApp isKindOfClass:wineApplication] ||
            ![NSApp respondsToSelector:NSSelectorFromString(@"setWineController:")]) {
            return NO;
        }
        if (eventMonitor) return YES;
        eventMonitor = [NSEvent addLocalMonitorForEventsMatchingMask:
            NSEventMaskMagnify | NSEventMaskBeginGesture | NSEventMaskEndGesture
            handler:^NSEvent *(NSEvent *event) { return HandleGesture(event); }];
        if (!eventMonitor) {
            bridgeState = @"monitor_unavailable";
            WriteStatus(YES);
            return YES;
        }
        focusObserver = [[NSNotificationCenter defaultCenter]
            addObserverForName:NSApplicationDidResignActiveNotification object:NSApp
            queue:nil usingBlock:^(NSNotification *notification) {
                (void)notification;
                ResetPinch(&pinch);
                targetWindowNumber = 0;
                Increment(&focusResets);
                WriteStatus(YES);
            }];
        terminationObserver = [[NSNotificationCenter defaultCenter]
            addObserverForName:NSApplicationWillTerminateNotification object:NSApp
            queue:nil usingBlock:^(NSNotification *notification) {
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
        return YES;
    }
}

static void ReadinessTick(CFRunLoopTimerRef timer, void *context) {
    (void)context;
    @autoreleasepool {
        if (readinessAttempts == 0) {
            // This is the first Objective-C work: already inside the main run loop.
            const char *rawPath = getenv("SC4_PINCH_STATUS");
            if (rawPath) {
                NSString *candidate = [[NSString alloc] initWithUTF8String:rawPath];
                if (candidate.isAbsolutePath) statusPath = candidate;
            }
            bridgeState = @"run_loop_callback";
            WriteStatus(YES);
        }
        ++readinessAttempts;
        if (InstallWhenWineIsReady() || readinessAttempts >= 240) {
            if (!eventMonitor && [bridgeState isEqualToString:@"run_loop_callback"]) {
                bridgeState = @"wine_not_ready";
                WriteStatus(YES);
            }
            CFRunLoopTimerInvalidate(timer);
            CFRelease(readinessTimer);
            readinessTimer = NULL;
        }
    }
}

__attribute__((constructor)) static void SC4PinchStart(void) {
    // Diagnostic bootstrap and process gates use C only, before any Objective-C messages.
    const char *enabled = getenv("SC4_PINCH_ENABLED");
    if (!enabled || strcmp(enabled, "1") != 0) return;
    int count = *_NSGetArgc();
    bool crtMatch = HasGameArgument(count, *_NSGetArgv());
    bool kernelQuerySucceeded = false;
    bool kernelMatch = KernelArgumentsMatch(&kernelQuerySucceeded);
    const char *rawPath = getenv("SC4_PINCH_STATUS");
    WriteBootstrap(rawPath, count, crtMatch, kernelMatch, kernelQuerySucceeded);
    if (!crtMatch && !kernelMatch) return;
    // A timer is serviced inside Wine's nested NSApp run loop, without a dispatch block.
    CFRunLoopTimerContext context = {0};
    readinessTimer = CFRunLoopTimerCreate(NULL, CFAbsoluteTimeGetCurrent() + 0.05,
                                          0.25, 0, 0, ReadinessTick, &context);
    if (readinessTimer) {
        CFRunLoopAddTimer(CFRunLoopGetMain(), readinessTimer, kCFRunLoopCommonModes);
        CFRunLoopWakeUp(CFRunLoopGetMain());
    }
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
