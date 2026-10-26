#import <Cocoa/Cocoa.h>
#import <ApplicationServices/ApplicationServices.h>
#include <libproc.h>
#include <sys/sysctl.h>
#include <math.h>

// Optional standalone fallback. No permissions are requested automatically.
// Only CGEventTapCreateForPid + the scroll-wheel event mask are used.
static const char *kWineRoot = "/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/wine/";
typedef struct { double x, y, time; int axis; BOOL fired, phased, ended, seen; } Swipe;
static Swipe swipe;
static uint64_t receivedEvents, zoomInSteps, zoomOutSteps, suppressedEvents, suppressedMomentum;
static void ResetSwipe(void) { memset(&swipe, 0, sizeof(swipe)); }

static CGEventRef FilterScroll(CGEventRef event) {
    CGEventFlags modifiers = kCGEventFlagMaskShift | kCGEventFlagMaskControl |
                            kCGEventFlagMaskAlternate | kCGEventFlagMaskCommand;
    int phase = (int)CGEventGetIntegerValueField(event, kCGScrollWheelEventScrollPhase);
    int momentum = (int)CGEventGetIntegerValueField(event, kCGScrollWheelEventMomentumPhase);
    BOOL continuous = CGEventGetIntegerValueField(event, kCGScrollWheelEventIsContinuous) != 0;
    if ((!continuous && !phase && !momentum) || (CGEventGetFlags(event) & modifiers)) {
        ResetSwipe();
        return event;
    }
    if (momentum) return swipe.axis == 2 ? event : NULL;
    double time = CGEventGetTimestamp(event) / 1e9;
    if (swipe.ended || (phase & kCGScrollPhaseBegan) || (phase & kCGScrollPhaseCancelled) ||
        (swipe.seen && (time < swipe.time || (!swipe.phased && !phase && time - swipe.time > 0.6))))
        ResetSwipe();
    swipe.ended = (phase & (kCGScrollPhaseEnded | kCGScrollPhaseCancelled)) != 0;
    if (phase & kCGScrollPhaseCancelled) return NULL;
    swipe.seen = YES;
    swipe.phased |= phase != 0;
    swipe.time = time;
    double x = CGEventGetDoubleValueField(event, kCGScrollWheelEventPointDeltaAxis2);
    double y = CGEventGetDoubleValueField(event, kCGScrollWheelEventPointDeltaAxis1);
    if (!isfinite(x) || !isfinite(y)) return event;
    swipe.x += x;
    swipe.y += y;
    if (!swipe.axis && fmax(fabs(swipe.x), fabs(swipe.y)) >= 4)
        swipe.axis = fabs(swipe.y) >= fabs(swipe.x) ? 1 : 2;
    if (swipe.axis == 2) return event;
    if (swipe.axis != 1 || swipe.fired || fabs(swipe.y) < 4) return NULL;
    swipe.fired = YES;
    int direction = swipe.y > 0 ? 1 : -1;
    if (direction > 0) ++zoomInSteps; else ++zoomOutSteps;
    // Wine 4.12: 20 native pixel units x 6 = WHEEL_DELTA 120, one notch.
    CGEventSetIntegerValueField(event, kCGScrollWheelEventIsContinuous, 1);
    CGEventSetIntegerValueField(event, kCGScrollWheelEventDeltaAxis1, direction);
    CGEventSetIntegerValueField(event, kCGScrollWheelEventDeltaAxis2, 0);
    CGEventSetIntegerValueField(event, kCGScrollWheelEventDeltaAxis3, 0);
    CGEventSetDoubleValueField(event, kCGScrollWheelEventFixedPtDeltaAxis1, direction);
    CGEventSetDoubleValueField(event, kCGScrollWheelEventFixedPtDeltaAxis2, 0);
    CGEventSetDoubleValueField(event, kCGScrollWheelEventFixedPtDeltaAxis3, 0);
    // CG's related setters can update other delta representations. Set Wine's
    // authoritative point fields last, after the line/fixed representations.
    CGEventSetIntegerValueField(event, kCGScrollWheelEventPointDeltaAxis1, direction * 20);
    CGEventSetIntegerValueField(event, kCGScrollWheelEventPointDeltaAxis2, 0);
    CGEventSetIntegerValueField(event, kCGScrollWheelEventPointDeltaAxis3, 0);
    return event;
}

static BOOL IsSimCity(pid_t pid) {
    char executable[PROC_PIDPATHINFO_MAXSIZE];
    if (proc_pidpath(pid, executable, sizeof(executable)) <= 0 ||
        strncmp(executable, kWineRoot, strlen(kWineRoot)) != 0) return NO;
    int mib[] = {CTL_KERN, KERN_PROCARGS2, pid};
    size_t length = 0;
    if (sysctl(mib, 3, NULL, &length, NULL, 0) != 0 || length < 5 || length > 2 * 1024 * 1024) return NO;
    char *data = malloc(length);
    if (!data) return NO;
    BOOL found = NO;
    if (sysctl(mib, 3, data, &length, NULL, 0) == 0 && length > 4) {
        int argc; memcpy(&argc, data, 4);
        char *end = data + length, *cursor = memchr(data + 4, 0, length - 4);
        if (cursor && argc > 0 && argc < 65536) {
            ++cursor;
            while (cursor < end && !*cursor) ++cursor;
            for (int i = 0; i < argc && cursor < end; ++i) {
                char *last = memchr(cursor, 0, end - cursor);
                if (!last) break;
                const char *base = cursor;
                for (const char *p = cursor; p < last; ++p)
                    if (*p == '/' || *p == '\\') base = p + 1;
                if (strcasecmp(base, "SimCity 4.exe") == 0) found = YES;
                cursor = last + 1;
            }
        }
    }
    free(data);
    return found;
}

#ifndef SC4_SCROLL_HELPER_TEST
@interface Helper : NSObject <NSApplicationDelegate> {
    NSWindow *_window;
    NSTextField *_status;
    NSButton *_start;
    NSTimer *_timer;
    CFMachPortRef _tap;
    CFRunLoopSourceRef _source;
    pid_t _pid;
    BOOL _requested;
    NSString *_lastError;
    NSDictionary *_lastStatus;
}
- (void)tick:(id)sender;
- (void)stopTap;
- (void)writeStatus;
- (CGEventRef)filter:(CGEventRef)event type:(CGEventType)type;
@end

static CGEventRef Callback(CGEventTapProxy proxy, CGEventType type, CGEventRef event, void *context) {
    (void)proxy;
    return [(__bridge Helper *)context filter:event type:type];
}

@implementation Helper
- (void)applicationDidFinishLaunching:(NSNotification *)notification {
    (void)notification;
    _requested = [NSProcessInfo.processInfo.arguments containsObject:@"--start"];
    _window = [[NSWindow alloc] initWithContentRect:NSMakeRect(0, 0, 540, 250)
        styleMask:NSWindowStyleMaskTitled | NSWindowStyleMaskClosable
        backing:NSBackingStoreBuffered defer:NO];
    _window.title = @"SimCity Trackpad Zoom";
    _window.releasedWhenClosed = NO;
    NSString *instructions = _requested ?
        @"Allow Accessibility for SimCity Trackpad Zoom, then return to the game.\n\nOne two-finger vertical swipe changes one zoom level. This helper handles SimCity scrolling only." :
        @"Scroll up or down with two fingers to change zoom by one level per swipe.\n\nEnable this app in macOS Accessibility settings, then click Start. This helper handles SimCity scrolling only.";
    NSTextField *description = [NSTextField wrappingLabelWithString:instructions];
    description.frame = NSMakeRect(24, 98, 492, 130);
    [_window.contentView addSubview:description];
    _status = [NSTextField labelWithString:@"Off — no scrolling is being changed."];
    _status.frame = NSMakeRect(24, 70, 492, 22);
    [_window.contentView addSubview:_status];
    NSButton *settings = [NSButton buttonWithTitle:@"Open Accessibility Settings" target:self action:@selector(settings:)];
    settings.frame = NSMakeRect(20, 22, 240, 32);
    [_window.contentView addSubview:settings];
    _start = [NSButton buttonWithTitle:@"Start" target:self action:@selector(start:)];
    _start.frame = NSMakeRect(310, 22, 95, 32);
    [_window.contentView addSubview:_start];
    NSButton *stop = [NSButton buttonWithTitle:@"Stop" target:self action:@selector(stop:)];
    stop.frame = NSMakeRect(415, 22, 95, 32);
    [_window.contentView addSubview:stop];
    [_window center]; [_window makeKeyAndOrderFront:nil];
    [NSApp activateIgnoringOtherApps:YES];
    _timer = [NSTimer scheduledTimerWithTimeInterval:1 target:self selector:@selector(tick:) userInfo:nil repeats:YES];
    [self tick:nil];
}
- (void)settings:(id)sender {
    (void)sender;
    // This request occurs only after the user clicks the settings button.
    // The user must still grant access in macOS; no preference is changed here.
    AXIsProcessTrustedWithOptions((__bridge CFDictionaryRef)@{
        (__bridge NSString *)kAXTrustedCheckOptionPrompt: @YES});
    [[NSWorkspace sharedWorkspace] openURL:[NSURL URLWithString:
        @"x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"]];
}
- (void)start:(id)sender { (void)sender; _lastError = nil; _requested = AXIsProcessTrusted(); [self tick:nil]; }
- (void)stop:(id)sender { (void)sender; _lastError = nil; _requested = NO; [self stopTap]; [self tick:nil]; }
- (void)stopTap {
    if (_tap) { CGEventTapEnable(_tap, false); CFMachPortInvalidate(_tap); }
    if (_source) { CFRunLoopRemoveSource(CFRunLoopGetMain(), _source, kCFRunLoopCommonModes); CFRelease(_source); _source = NULL; }
    if (_tap) { CFRelease(_tap); _tap = NULL; }
    _pid = 0; ResetSwipe();
}
- (void)tick:(id)sender {
    [self update:sender];
    [self writeStatus];
}
- (void)writeStatus {
    NSDictionary *state = @{@"schema": @1, @"helper_pid": @(getpid()),
        @"accessibility_trusted": @(AXIsProcessTrusted()), @"requested": @(_requested),
        @"target_pid": @(_pid), @"tap_active": @(_tap && CGEventTapIsEnabled(_tap)),
        @"received_events": @(receivedEvents), @"zoom_in_steps": @(zoomInSteps),
        @"zoom_out_steps": @(zoomOutSteps), @"suppressed_events": @(suppressedEvents),
        @"suppressed_momentum": @(suppressedMomentum), @"message": _status.stringValue ?: @"Off"};
    if ([_lastStatus isEqualToDictionary:state]) return;
    _lastStatus = state;
    NSMutableDictionary *output = [state mutableCopy];
    output[@"updated_unix_seconds"] = @([NSDate date].timeIntervalSince1970);
    NSString *path = @"/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Mac Trackpad Zoom status.json";
    [[NSFileManager defaultManager] createDirectoryAtPath:path.stringByDeletingLastPathComponent
        withIntermediateDirectories:YES attributes:nil error:NULL];
    NSData *json = [NSJSONSerialization dataWithJSONObject:output options:0 error:NULL];
    [json writeToFile:path options:NSDataWritingAtomic error:NULL];
}
- (void)update:(id)sender {
    (void)sender;
    BOOL trusted = AXIsProcessTrusted(); // Read only; never displays a permission prompt.
    _start.enabled = trusted && !_requested;
    if (!_requested || !trusted) {
        [self stopTap];
        _status.stringValue = _lastError ?: (trusted ? @"Off — click Start to enable the helper." : @"Off — Accessibility access has not been enabled.");
        return;
    }
    if (_pid && IsSimCity(_pid) && _tap && CFMachPortIsValid(_tap)) return;
    [self stopTap];
    pid_t selected = 0;
    int count = proc_listallpids(NULL, 0);
    if (count > 0 && count < 1000000) {
        size_t capacity = (size_t)count + 128;
        pid_t *pids = calloc(capacity, sizeof(pid_t));
        if (pids) {
            int actual = proc_listallpids(pids, (int)(capacity * sizeof(pid_t)));
            if (actual > 0) for (int i = 0; i < actual && (size_t)i < capacity; ++i)
                if (pids[i] > 0 && IsSimCity(pids[i])) { selected = pids[i]; break; }
            free(pids);
        }
    }
    if (!selected) { _status.stringValue = @"Waiting for SimCity 4. Other apps are unaffected."; return; }
    _tap = CGEventTapCreateForPid(selected, kCGHeadInsertEventTap, kCGEventTapOptionDefault,
                                CGEventMaskBit(kCGEventScrollWheel), Callback, (__bridge void *)self);
    if (!_tap) { _requested = NO; _lastError = @"Could not attach. The helper remains off."; _status.stringValue = _lastError; return; }
    _source = CFMachPortCreateRunLoopSource(NULL, _tap, 0);
    if (!_source) { [self stopTap]; _requested = NO; _lastError = @"Could not attach. The helper remains off."; _status.stringValue = _lastError; return; }
    _pid = selected;
    CFRunLoopAddSource(CFRunLoopGetMain(), _source, kCFRunLoopCommonModes);
    CGEventTapEnable(_tap, true);
    _status.stringValue = @"On — one zoom step per vertical swipe in SimCity.";
}
- (CGEventRef)filter:(CGEventRef)event type:(CGEventType)type {
    if (type == kCGEventTapDisabledByTimeout) { if (_tap) CGEventTapEnable(_tap, true); ResetSwipe(); return event; }
    if (type == kCGEventTapDisabledByUserInput) { _requested = NO; return event; }
    if (type != kCGEventScrollWheel || !_requested) return event;
    pid_t destination = (pid_t)CGEventGetIntegerValueField(event, kCGEventTargetUnixProcessID);
    // The tap is already specific to _pid. Reject conflicting populated metadata.
    if (destination && destination != _pid) {
        ResetSwipe(); return event;
    }
    ++receivedEvents;
    CGEventRef filtered = FilterScroll(event);
    if (!filtered) {
        ++suppressedEvents;
        if (CGEventGetIntegerValueField(event, kCGScrollWheelEventMomentumPhase)) ++suppressedMomentum;
    }
    return filtered;
}
- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender { (void)sender; return YES; }
- (void)applicationWillTerminate:(NSNotification *)notification { (void)notification; [_timer invalidate]; _requested = NO; [self stopTap]; _status.stringValue = @"Stopped"; [self writeStatus]; }
@end

int main(void) {
    @autoreleasepool {
        [NSApplication sharedApplication];
        Helper *helper = [Helper new]; NSApp.delegate = helper;
        [NSApp run];
    }
    return 0;
}
#else
#include <assert.h>
static CGEventRef TestEvent(int delta, int phase, int momentum, double time) {
    CGEventRef e = CGEventCreateScrollWheelEvent(NULL, kCGScrollEventUnitPixel, 2, delta, 0);
    CGEventSetIntegerValueField(e, kCGScrollWheelEventScrollPhase, phase);
    CGEventSetIntegerValueField(e, kCGScrollWheelEventMomentumPhase, momentum);
    CGEventSetTimestamp(e, (uint64_t)(time * 1e9)); return e;
}
int main(void) {
    @autoreleasepool {
        assert(NSApp == nil);
        CGEventRef e = TestEvent(8, kCGScrollPhaseBegan, 0, 1);
        assert(FilterScroll(e) == e);
        assert(CGEventGetIntegerValueField(e, kCGScrollWheelEventPointDeltaAxis1) == 20); CFRelease(e);
        e = TestEvent(800, kCGScrollPhaseChanged, 0, 1.1); assert(!FilterScroll(e)); CFRelease(e);
        e = TestEvent(0, kCGScrollPhaseEnded, 0, 1.2); assert(!FilterScroll(e)); CFRelease(e);
        e = TestEvent(800, 0, kCGMomentumScrollPhaseBegin, 1.3); assert(!FilterScroll(e)); CFRelease(e);
        e = TestEvent(-8, kCGScrollPhaseBegan, 0, 2); assert(FilterScroll(e) == e);
        assert(CGEventGetIntegerValueField(e, kCGScrollWheelEventPointDeltaAxis1) == -20); CFRelease(e);
        e = CGEventCreateScrollWheelEvent(NULL, kCGScrollEventUnitLine, 1, 1);
        assert(FilterScroll(e) == e); CFRelease(e);
        e = TestEvent(800, kCGScrollPhaseBegan, 0, 3);
        CGEventSetFlags(e, kCGEventFlagMaskControl);
        assert(FilterScroll(e) == e);
        assert(CGEventGetIntegerValueField(e, kCGScrollWheelEventPointDeltaAxis1) == 800); CFRelease(e);
        e = TestEvent(0, kCGScrollPhaseBegan, 0, 4);
        CGEventSetIntegerValueField(e, kCGScrollWheelEventPointDeltaAxis2, 10);
        assert(FilterScroll(e) == e); CFRelease(e);
        e = TestEvent(100, kCGScrollPhaseChanged, 0, 4.1);
        assert(FilterScroll(e) == e); CFRelease(e);
        e = TestEvent(0, kCGScrollPhaseEnded, 0, 4.2);
        assert(FilterScroll(e) == e); CFRelease(e);
        e = TestEvent(100, 0, kCGMomentumScrollPhaseContinue, 4.3);
        assert(FilterScroll(e) == e); CFRelease(e);
        e = TestEvent(5, kCGScrollPhaseBegan, 0, 5);
        assert(FilterScroll(e) == e); CFRelease(e);
        e = TestEvent(-800, kCGScrollPhaseChanged, 0, 8);
        assert(!FilterScroll(e)); CFRelease(e);
        assert(NSApp == nil);
        puts("PASS: pure local CG-event normalization only; no app launched, tap created, permission checked, or input posted.");
    }
}
#endif
