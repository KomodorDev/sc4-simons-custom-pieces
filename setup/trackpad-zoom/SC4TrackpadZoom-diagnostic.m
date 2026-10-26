#import <Cocoa/Cocoa.h>
#import <objc/runtime.h>
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
#include <time.h>
#include <unistd.h>

// No system event tap or input-posting permission is used. Events stay in NSApp.
static const double kGestureGap = 0.6;
static const double kScrollPointThreshold = 4.0;

typedef struct {
    double accumulated;
    double lastTime;
    bool hasEvent;
    bool fired;
    bool phased;
} GestureState;

static void ResetGesture(GestureState *state) {
    memset(state, 0, sizeof(*state));
}

static int AdvanceGesture(GestureState *state, double amount, double timestamp,
                          bool began, bool ended, bool cancelled, bool hasPhase,
                          double threshold) {
    if (cancelled || !isfinite(amount) || !isfinite(timestamp)) {
        ResetGesture(state);
        return 0;
    }
    if (began || (state->hasEvent &&
                  (timestamp < state->lastTime ||
                   (!state->phased && !hasPhase && timestamp - state->lastTime > kGestureGap)))) {
        ResetGesture(state);
    }
    state->phased = state->phased || hasPhase;
    state->hasEvent = true;
    state->lastTime = timestamp;
    int step = 0;
    if (!state->fired) {
        state->accumulated += amount;
        if (state->accumulated >= threshold) step = 1;
        else if (state->accumulated <= -threshold) step = -1;
        if (step) state->fired = true;
    }
    if (ended) ResetGesture(state);
    return step;
}

static int AdvanceScroll(GestureState *state, double amount, double timestamp,
                         bool began, bool ended, bool cancelled, bool hasPhase) {
    return AdvanceGesture(state, amount, timestamp, began, ended, cancelled, hasPhase,
                          kScrollPointThreshold);
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

// Wine's handler reads the CGEvent directly, so normalizing only deltaY is insufficient.
// This proxy is passed solely to that verified Objective-C method, never to AppKit.
@interface SC4NormalizedScrollEvent : NSProxy {
    NSEvent *_source;
    CGEventRef _normalized;
    int _direction;
}
- (instancetype)initWithEvent:(NSEvent *)event direction:(int)direction;
@end

@implementation SC4NormalizedScrollEvent
- (instancetype)initWithEvent:(NSEvent *)event direction:(int)direction {
    if (!event.CGEvent) return nil;
    _source = event;
    _direction = direction > 0 ? 1 : -1;
    _normalized = CGEventCreateCopy(event.CGEvent);
    if (!_normalized) return nil;
    CGEventSetIntegerValueField(_normalized, kCGScrollWheelEventIsContinuous, 1);
    CGEventSetDoubleValueField(_normalized, kCGScrollWheelEventPointDeltaAxis1, _direction * 20.0);
    CGEventSetDoubleValueField(_normalized, kCGScrollWheelEventPointDeltaAxis2, 0);
    CGEventSetDoubleValueField(_normalized, kCGScrollWheelEventPointDeltaAxis3, 0);
    return self;
}
- (void)dealloc { if (_normalized) CFRelease(_normalized); }
- (CGEventRef)CGEvent { return _normalized; }
- (NSWindow *)window { return _source.window; }
- (NSTimeInterval)timestamp { return _source.timestamp; }
- (CGFloat)deltaX { return 0; }
- (CGFloat)deltaY { return _direction; }
- (BOOL)hasPreciseScrollingDeltas { return NO; }
- (NSMethodSignature *)methodSignatureForSelector:(SEL)selector {
    return [_source methodSignatureForSelector:selector];
}
- (void)forwardInvocation:(NSInvocation *)invocation { [invocation invokeWithTarget:_source]; }
@end

#ifndef SC4_TRACKPAD_TEST

static GestureState scrolling;
static id focusObserver;
static id terminationObserver;
static NSString *statusPath;
static char *bootstrapStatusPath;
static const char *checkpointState = "constructor";
static double lastCheckpointTime;
static BOOL lateStatusEnvironmentPresent;
static uint64_t scrollHandlerEntries, ordinaryWheelEvents, eligibleScrollEvents;
static uint64_t inactiveEvents, noKeyWindowEvents, nonWineWindowEvents;
static uint64_t otherEventWindowEvents, otherTitleEvents, modifiedEvents;
static NSString *bridgeState = @"waiting_for_wine";
static uint64_t focusResets;
static NSInteger targetWindowNumber;
static double lastStatusTime;
typedef void (*ApplicationRunHandler)(id, SEL);
static ApplicationRunHandler originalApplicationRun;
static Method applicationRunMethod;
static BOOL runStartupHookInstalled;
typedef void (*ScrollHandler)(id, SEL, NSEvent *);
static ScrollHandler originalScrollHandler;
static Method scrollMethod;
static BOOL scrollHookInstalled;
static uint64_t scrollEvents, scrollUpSteps, scrollDownSteps, momentumSuppressed, scrollProxyFailures;
static double directionX, directionY;
static int scrollAxis; // 0 undecided, 1 vertical, 2 horizontal
static BOOL scrollEnded;
static uint64_t horizontalPassthrough;

static void ResetScrolling(void) {
    ResetGesture(&scrolling);
    directionX = directionY = 0;
    scrollAxis = 0;
    scrollEnded = NO;
}

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
        "\"kernel_query_succeeded\":%s,\"kernel_argument_match\":%s,\"accepted\":%s,"
        "\"run_startup_hook_installed\":%s,\"status_path_captured\":%s}\n",
        (long)getpid(), argumentCount, crtMatch ? "true" : "false",
        kernelQuerySucceeded ? "true" : "false", kernelMatch ? "true" : "false",
        (crtMatch || kernelMatch) ? "true" : "false",
        runStartupHookInstalled ? "true" : "false", bootstrapStatusPath ? "true" : "false");
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

// Keep our own immutable copy; Wine may replace the native environment later.
static BOOL CaptureStatusPath(const char *path) {
    if (bootstrapStatusPath) return YES;
    if (!path || path[0] != '/' || strlen(path) > 3500) return NO;
    bootstrapStatusPath = strdup(path);
    return bootstrapStatusPath != NULL;
}

// C-only checkpoint before any Objective-C work at run entry. Counters are
// limited to our own handler and written at most four times/sec during input.
static void WriteRunCheckpoint(const char *state, BOOL force) {
    if (state) checkpointState = state;
    if (!bootstrapStatusPath) return;
    struct timespec clockValue;
    if (clock_gettime(CLOCK_MONOTONIC, &clockValue) != 0) return;
    double now = clockValue.tv_sec + clockValue.tv_nsec / 1000000000.0;
    if (!force && now - lastCheckpointTime < 0.25) return;
    lastCheckpointTime = now;
    char output[4096], temporary[4096], json[1536];
    int n = snprintf(output, sizeof(output), "%s.run.%ld.json", bootstrapStatusPath, (long)getpid());
    if (n < 0 || (size_t)n >= sizeof(output)) return;
    n = snprintf(temporary, sizeof(temporary), "%s.XXXXXX", output);
    if (n < 0 || (size_t)n >= sizeof(temporary)) return;
    n = snprintf(json, sizeof(json),
        "{\"schema\":1,\"pid\":%ld,\"state\":\"%s\",\"scroll_hook_installed\":%s,"
        "\"late_status_environment_present\":%s,\"scroll_handler_entries\":%llu,"
        "\"ordinary_wheel_events\":%llu,\"eligible_scroll_events\":%llu,"
        "\"inactive_events\":%llu,\"no_key_window_events\":%llu,\"non_wine_window_events\":%llu,"
        "\"other_event_window_events\":%llu,\"other_title_events\":%llu,\"modified_events\":%llu,"
        "\"up_steps\":%llu,\"down_steps\":%llu,\"momentum_suppressed\":%llu}\n",
        (long)getpid(), checkpointState, scrollHookInstalled ? "true" : "false",
        lateStatusEnvironmentPresent ? "true" : "false",
        (unsigned long long)scrollHandlerEntries, (unsigned long long)ordinaryWheelEvents,
        (unsigned long long)eligibleScrollEvents, (unsigned long long)inactiveEvents,
        (unsigned long long)noKeyWindowEvents, (unsigned long long)nonWineWindowEvents,
        (unsigned long long)otherEventWindowEvents, (unsigned long long)otherTitleEvents,
        (unsigned long long)modifiedEvents, (unsigned long long)scrollUpSteps,
        (unsigned long long)scrollDownSteps, (unsigned long long)momentumSuppressed);
    if (n < 0 || (size_t)n >= sizeof(json)) return;
    int fd = mkstemp(temporary);
    if (fd < 0) return;
    size_t written = 0;
    while (written < (size_t)n) {
        ssize_t amount = write(fd, json + written, (size_t)n - written);
        if (amount < 0 && errno == EINTR) continue;
        if (amount <= 0) break;
        written += (size_t)amount;
    }
    BOOL complete = written == (size_t)n;
    if (close(fd) != 0) complete = NO;
    if (!complete || rename(temporary, output) != 0) unlink(temporary);
}

static void Increment(uint64_t *counter) {
    if (*counter < UINT64_MAX) ++*counter;
}

static void WriteStatus(BOOL force) {
    WriteRunCheckpoint(NULL, force);
    if (!statusPath) return;
    double now = NSProcessInfo.processInfo.systemUptime;
    if (!force && now - lastStatusTime < 0.25) return;
    lastStatusTime = now;
    // Only this bridge's state and counters are recorded, never keys or window text.
    NSDictionary *status = @{
        @"schema": @1, @"pid": @(getpid()), @"state": bridgeState,
        @"scroll_handler_entries": @(scrollHandlerEntries),
        @"ordinary_wheel_events": @(ordinaryWheelEvents), @"eligible_scroll_events": @(eligibleScrollEvents),
        @"inactive_events": @(inactiveEvents), @"no_key_window_events": @(noKeyWindowEvents),
        @"non_wine_window_events": @(nonWineWindowEvents),
        @"other_event_window_events": @(otherEventWindowEvents),
        @"other_title_events": @(otherTitleEvents), @"modified_events": @(modifiedEvents),
        @"late_status_environment_present": @(lateStatusEnvironmentPresent),
        @"focus_resets": @(focusResets),
        @"scroll_events": @(scrollEvents), @"scroll_up_steps": @(scrollUpSteps),
        @"scroll_down_steps": @(scrollDownSteps), @"momentum_suppressed": @(momentumSuppressed),
        @"scroll_proxy_failures": @(scrollProxyFailures), @"scroll_threshold_points": @(kScrollPointThreshold),
        @"horizontal_passthrough": @(horizontalPassthrough),
        @"scroll_hook_installed": @(scrollHookInstalled),
        @"updated_unix_seconds": @([NSDate date].timeIntervalSince1970)
    };
    NSData *data = [NSJSONSerialization dataWithJSONObject:status options:0 error:NULL];
    if (data) [data writeToFile:statusPath options:NSDataWritingAtomic error:NULL];
}

static BOOL EligibleScrollWindow(NSEvent *event) {
    NSWindow *window = NSApp.keyWindow;
    Class wineWindow = NSClassFromString(@"WineWindow");
    NSEventModifierFlags excluded = NSEventModifierFlagCommand | NSEventModifierFlagShift |
                                   NSEventModifierFlagControl | NSEventModifierFlagOption;
    if (!NSApp.isActive) { Increment(&inactiveEvents); return NO; }
    if (!window) { Increment(&noKeyWindowEvents); return NO; }
    if (!wineWindow || ![window isKindOfClass:wineWindow]) {
        Increment(&nonWineWindowEvents); return NO;
    }
    if (event.window && event.window != window) { Increment(&otherEventWindowEvents); return NO; }
    if ([window.title caseInsensitiveCompare:@"SimCity 4"] != NSOrderedSame) {
        Increment(&otherTitleEvents); return NO;
    }
    if (event.modifierFlags & excluded) { Increment(&modifiedEvents); return NO; }
    return YES;
}

static void SC4HandleScrollWheel(id controller, SEL selector, NSEvent *event) {
    Increment(&scrollHandlerEntries);
    BOOL touchScroll = event.hasPreciseScrollingDeltas || event.phase != NSEventPhaseNone ||
                       event.momentumPhase != NSEventPhaseNone;
    if (!touchScroll) Increment(&ordinaryWheelEvents);
    if (!touchScroll || !EligibleScrollWindow(event)) {
        WriteStatus(NO);
        ResetScrolling();
        targetWindowNumber = 0;
        originalScrollHandler(controller, selector, event);
        return;
    }
    Increment(&eligibleScrollEvents);
    if (targetWindowNumber != NSApp.keyWindow.windowNumber) {
        ResetScrolling();
        targetWindowNumber = NSApp.keyWindow.windowNumber;
    }
    Increment(&scrollEvents);
    if (event.momentumPhase != NSEventPhaseNone) {
        if (scrollAxis == 2) {
            originalScrollHandler(controller, selector, event);
            Increment(&horizontalPassthrough);
        } else {
            // Vertical momentum must never create another zoom step.
            Increment(&momentumSuppressed);
        }
        WriteStatus(event.momentumPhase == NSEventPhaseEnded);
        return;
    }
    NSEventPhase phase = event.phase;
    BOOL began = (phase & NSEventPhaseBegan) != 0;
    BOOL ended = (phase & NSEventPhaseEnded) != 0;
    BOOL cancelled = (phase & NSEventPhaseCancelled) != 0;
    BOOL phased = phase != NSEventPhaseNone;
    if (scrollEnded || began || cancelled ||
        (scrolling.hasEvent && (event.timestamp < scrolling.lastTime ||
         (!scrolling.phased && !phased && event.timestamp - scrolling.lastTime > kGestureGap)))) {
        ResetScrolling();
    }
    scrollEnded = ended || cancelled;
    if (cancelled) return;
    int step = AdvanceScroll(&scrolling, event.scrollingDeltaY, event.timestamp,
                             false, ended, false, phased);
    if (scrollAxis == 0) {
        directionX += event.scrollingDeltaX;
        directionY += event.scrollingDeltaY;
        if (fmax(fabs(directionX), fabs(directionY)) >= kScrollPointThreshold) {
            scrollAxis = fabs(directionY) >= fabs(directionX) ? 1 : 2;
        }
    }
    if (scrollAxis == 2) {
        originalScrollHandler(controller, selector, event);
        Increment(&horizontalPassthrough);
    } else if (scrollAxis == 1 && step) {
        SC4NormalizedScrollEvent *normalized = [[SC4NormalizedScrollEvent alloc]
            initWithEvent:event direction:step];
        if (normalized) {
            originalScrollHandler(controller, selector, (NSEvent *)normalized);
            Increment(step > 0 ? &scrollUpSteps : &scrollDownSteps);
        } else {
            Increment(&scrollProxyFailures);
            originalScrollHandler(controller, selector, event);
        }
    }
    WriteStatus(step != 0 || (phase & (NSEventPhaseEnded | NSEventPhaseCancelled)) != 0);
}

static BOOL InstallScrollHook(void) {
    if (scrollHookInstalled) return YES;
    Class controllerClass = NSClassFromString(@"WineApplicationController");
    Method method = controllerClass ? class_getInstanceMethod(controllerClass,
                                        NSSelectorFromString(@"handleScrollWheel:")) : NULL;
    if (!method || method_getNumberOfArguments(method) != 3) return NO;
    char *returnType = method_copyReturnType(method);
    char *argumentType = method_copyArgumentType(method, 2);
    BOOL signatureMatches = returnType && returnType[0] == 'v' && argumentType && argumentType[0] == '@';
    free(returnType);
    free(argumentType);
    if (!signatureMatches) return NO;
    originalScrollHandler = (ScrollHandler)method_getImplementation(method);
    if (!originalScrollHandler) return NO;
    scrollMethod = method;
    method_setImplementation(scrollMethod, (IMP)SC4HandleScrollWheel);
    scrollHookInstalled = YES;
    return YES;
}

static BOOL InstallWhenWineIsReady(void) {
    @autoreleasepool {
        Class wineApplication = NSClassFromString(@"WineApplication");
        if (!NSApp || !wineApplication || ![NSApp isKindOfClass:wineApplication] ||
            ![NSApp respondsToSelector:NSSelectorFromString(@"setWineController:")]) {
            return NO;
        }
        if (scrollHookInstalled) return YES;
        if (!InstallScrollHook()) {
            bridgeState = @"scroll_handler_not_ready";
            WriteStatus(NO);
            return NO;
        }
        focusObserver = [[NSNotificationCenter defaultCenter]
            addObserverForName:NSApplicationDidResignActiveNotification object:NSApp
            queue:nil usingBlock:^(NSNotification *notification) {
                (void)notification;
                ResetScrolling();
                targetWindowNumber = 0;
                Increment(&focusResets);
                WriteStatus(YES);
            }];
        terminationObserver = [[NSNotificationCenter defaultCenter]
            addObserverForName:NSApplicationWillTerminateNotification object:NSApp
            queue:nil usingBlock:^(NSNotification *notification) {
                (void)notification;
                if (focusObserver) [[NSNotificationCenter defaultCenter] removeObserver:focusObserver];
                focusObserver = nil;
                ResetScrolling();
                if (scrollMethod && method_getImplementation(scrollMethod) == (IMP)SC4HandleScrollWheel) {
                    method_setImplementation(scrollMethod, (IMP)originalScrollHandler);
                }
                scrollHookInstalled = NO;
                bridgeState = @"stopped";
                WriteStatus(YES);
            }];
        bridgeState = @"scroll_hook_installed";
        WriteStatus(YES);
        return YES;
    }
}

// Wine 4.12 creates WineApplication and sets its controller before invoking the
// inherited NSApplication -run. Attach at that exact point; do not create NSApp,
// queue a block, or depend on an early constructor's CFRunLoop identity.
static void SC4ApplicationRun(id application, SEL selector) {
    // Do not rely on Foundation or a late getenv for evidence that this ran.
    WriteRunCheckpoint("application_run_entered_c", YES);
    ApplicationRunHandler run = originalApplicationRun;
    if (applicationRunMethod &&
        method_getImplementation(applicationRunMethod) == (IMP)SC4ApplicationRun) {
        method_setImplementation(applicationRunMethod, (IMP)run);
    }
    runStartupHookInstalled = NO;
    @autoreleasepool {
        lateStatusEnvironmentPresent = getenv("SC4_TRACKPAD_STATUS") != NULL;
        if (bootstrapStatusPath) {
            NSString *candidate = [[NSString alloc] initWithUTF8String:bootstrapStatusPath];
            if (candidate.isAbsolutePath) statusPath = candidate;
        }
        bridgeState = @"application_run_entered";
        WriteStatus(YES);
        if (application != NSApp || !InstallWhenWineIsReady()) {
            bridgeState = @"wine_not_ready_at_run";
            WriteStatus(YES);
        }
    }
    WriteRunCheckpoint(scrollHookInstalled ? "scroll_hook_installed_c" : "scroll_hook_unavailable_c", YES);
    // Preserve the original NSApplication event loop, including Mac full screen.
    run(application, selector);
}

static BOOL InstallRunStartupHook(void) {
    if (runStartupHookInstalled) return YES;
    Class applicationClass = objc_getClass("NSApplication");
    Method method = applicationClass ? class_getInstanceMethod(applicationClass,
                                         sel_registerName("run")) : NULL;
    if (!method || method_getNumberOfArguments(method) != 2) return NO;
    char *returnType = method_copyReturnType(method);
    BOOL signatureMatches = returnType && returnType[0] == 'v';
    free(returnType);
    if (!signatureMatches) return NO;
    originalApplicationRun = (ApplicationRunHandler)method_getImplementation(method);
    if (!originalApplicationRun || originalApplicationRun == SC4ApplicationRun) return NO;
    applicationRunMethod = method;
    method_setImplementation(applicationRunMethod, (IMP)SC4ApplicationRun);
    runStartupHookInstalled = YES;
    return YES;
}

__attribute__((constructor)) static void SC4TrackpadStart(void) {
    // Diagnostic bootstrap and process gates use C only, before any Objective-C messages.
    const char *enabled = getenv("SC4_TRACKPAD_ENABLED");
    if (!enabled || strcmp(enabled, "1") != 0) return;
    int count = *_NSGetArgc();
    bool crtMatch = HasGameArgument(count, *_NSGetArgv());
    bool kernelQuerySucceeded = false;
    bool kernelMatch = KernelArgumentsMatch(&kernelQuerySucceeded);
    const char *rawPath = getenv("SC4_TRACKPAD_STATUS");
    WriteBootstrap(rawPath, count, crtMatch, kernelMatch, kernelQuerySucceeded);
    if (!crtMatch && !kernelMatch) return;
    CaptureStatusPath(rawPath);
    // Runtime inspection only: no Objective-C messages or NSApplication creation.
    InstallRunStartupHook();
    WriteBootstrap(rawPath, count, crtMatch, kernelMatch, kernelQuerySucceeded);
}

#else

#include <assert.h>
#include <stdio.h>

int main(void) {
    GestureState state = {0};
    assert(AdvanceScroll(&state, 1.5, 4.0, true, false, false, true) == 0);
    assert(AdvanceScroll(&state, 2.5, 4.1, false, false, false, true) == 1);
    assert(AdvanceScroll(&state, 80, 4.2, false, false, false, true) == 0);
    assert(AdvanceScroll(&state, 80, 5.0, false, false, false, true) == 0);
    assert(AdvanceScroll(&state, 0, 5.1, false, true, false, true) == 0);
    assert(AdvanceScroll(&state, -4, 5.2, true, false, false, true) == -1);
    ResetGesture(&state);
    assert(AdvanceScroll(&state, 4, 6.0, false, false, false, false) == 1);
    assert(AdvanceScroll(&state, -4, 6.7, false, false, false, false) == -1);
    assert(IsGameArgument("SimCity 4.exe"));
    assert(IsGameArgument("C:\\Games\\SimCity 4.exe"));
    assert(IsGameArgument("/game/SimCity 4.exe"));
    assert(!IsGameArgument("echo SimCity 4.exe"));
    assert(!IsGameArgument("SimCity 4.exe.bak"));
    char *args[] = {"wine32on64", "C:\\Games\\SimCity 4.exe", "-w"};
    assert(HasGameArgument(3, args));
    @autoreleasepool {
        assert(NSApp == nil);
        CGEventRef raw = CGEventCreateScrollWheelEvent(NULL, kCGScrollEventUnitPixel, 2, 300, 50);
        assert(raw);
        CGEventSetLocation(raw, CGPointMake(123, 456));
        NSEvent *source = [NSEvent eventWithCGEvent:raw];
        assert(source);
        for (int direction = -1; direction <= 1; direction += 2) {
            SC4NormalizedScrollEvent *proxy = [[SC4NormalizedScrollEvent alloc]
                initWithEvent:source direction:direction];
            assert(proxy && [proxy CGEvent] != raw);
            assert(CGEventGetIntegerValueField([proxy CGEvent], kCGScrollWheelEventIsContinuous) == 1);
            double y = CGEventGetDoubleValueField([proxy CGEvent], kCGScrollWheelEventPointDeltaAxis1);
            assert(y * 6 == direction * 120);
            assert(CGEventGetDoubleValueField([proxy CGEvent], kCGScrollWheelEventPointDeltaAxis2) == 0);
            assert(CGPointEqualToPoint(CGEventGetLocation([proxy CGEvent]), CGPointMake(123, 456)));
            assert(proxy.window == source.window && proxy.timestamp == source.timestamp);
            assert(!proxy.hasPreciseScrollingDeltas);
            assert([(NSEvent *)proxy modifierFlags] == source.modifierFlags);
        }
        assert(CGEventGetDoubleValueField(raw, kCGScrollWheelEventPointDeltaAxis1) == 300);
        CFRelease(raw);
        assert(NSApp == nil);
    }
    puts("PASS: scroll state, process arguments, and exact 120-unit scroll proxy; no NSApp created or events posted.");
    return 0;
}

#endif
