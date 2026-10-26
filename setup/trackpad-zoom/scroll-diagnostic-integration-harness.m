// Runs the production hook against fake Objective-C objects only. It creates no
// NSApplication, windows, event taps, or input posted to another process.
#include "SC4TrackpadZoom-diagnostic.m"
#include <assert.h>

@interface WineWindow : NSObject
@property(nonatomic, copy) NSString *title;
@property(nonatomic) NSInteger windowNumber;
@end
@implementation WineWindow
@end

@interface WineApplication : NSObject
@property(nonatomic) BOOL isActive;
@property(nonatomic, strong) WineWindow *keyWindow;
- (void)setWineController:(id)controller;
@end
@implementation WineApplication
- (void)setWineController:(id)controller { (void)controller; }
@end

@interface HarnessScrollEvent : NSObject {
    CGEventRef _raw;
}
@property(nonatomic, strong) WineWindow *window;
@property(nonatomic) NSTimeInterval timestamp;
@property(nonatomic) NSEventPhase phase;
@property(nonatomic) NSEventPhase momentumPhase;
@property(nonatomic) NSEventModifierFlags modifierFlags;
@property(nonatomic) BOOL hasPreciseScrollingDeltas;
@property(nonatomic) CGFloat scrollingDeltaY;
@property(nonatomic) CGFloat scrollingDeltaX;
@property(nonatomic, readonly) CGEventRef CGEvent;
- (instancetype)initWithDelta:(double)delta time:(double)time window:(WineWindow *)window;
@end
@implementation HarnessScrollEvent
- (instancetype)initWithDelta:(double)delta time:(double)time window:(WineWindow *)window {
    self = [super init];
    if (self) {
        _raw = CGEventCreateScrollWheelEvent(NULL, kCGScrollEventUnitPixel, 2, 0, 0);
        assert(_raw);
        CGEventSetDoubleValueField(_raw, kCGScrollWheelEventPointDeltaAxis1, delta);
        CGEventSetLocation(_raw, CGPointMake(123, 456));
        _scrollingDeltaY = delta;
        _timestamp = time;
        _window = window;
        _hasPreciseScrollingDeltas = YES;
    }
    return self;
}
- (CGEventRef)CGEvent { return _raw; }
- (CGFloat)deltaX { return _scrollingDeltaX; }
- (CGFloat)deltaY { return _scrollingDeltaY; }
- (void)dealloc { if (_raw) CFRelease(_raw); }
@end

static NSUInteger originalCalls, normalizedCalls, passedThroughCalls;
static NSEvent *inputEvent;
static double lastWindowsDelta, debt;
static BOOL emulatePrecise = YES;
static NSInteger checkedWindowNumber;
static double nextHorizontalDelta;
static NSUInteger originalRunCalls;
static id originalRunReceiver;
static void HarnessOriginalRun(id application, SEL selector) {
    assert(selector == @selector(run));
    ++originalRunCalls;
    originalRunReceiver = application;
    assert(!runStartupHookInstalled);
    assert(method_getImplementation(applicationRunMethod) == (IMP)HarnessOriginalRun);
}

@interface WineApplicationController : NSObject
- (void)handleScrollWheel:(NSEvent *)event;
@end
@implementation WineApplicationController
- (void)handleScrollWheel:(NSEvent *)event {
    ++originalCalls;
    if (event == inputEvent) {
        ++passedThroughCalls;
        return;
    }
    ++normalizedCalls;
    CGEventRef cg = event.CGEvent;
    assert(cg);
    assert(CGEventGetIntegerValueField(cg, kCGScrollWheelEventIsContinuous) == 1);
    // Wine 4.12 cocoa_app.m converts CG point deltas to Win32 units by x6.
    // The normalized CG delta must therefore be 20, not 120.
    double y = CGEventGetDoubleValueField(cg, kCGScrollWheelEventPointDeltaAxis1) * 6;
    assert(y == 120 || y == -120);
    assert(CGEventGetDoubleValueField(cg, kCGScrollWheelEventPointDeltaAxis2) == 0);
    assert(CGPointEqualToPoint(CGEventGetLocation(cg), CGPointMake(123, 456)));
    assert(event.window == inputEvent.window);
    assert(event.timestamp == inputEvent.timestamp);
    assert(event.modifierFlags == inputEvent.modifierFlags);
    checkedWindowNumber = event.window.windowNumber;
    lastWindowsDelta = y;
    if (!emulatePrecise) {
        // Wine's non-precise debt branch, including possible prior wheel debt.
        if ((debt < 0 && y < 0) || (debt > 0 && y > 0)) debt = 0;
        debt += y;
        lastWindowsDelta = debt > 0 && y > 0 ? 120 * ceil(debt / 120) :
                           debt < 0 && y < 0 ? -120 * ceil(-debt / 120) : 0;
        debt -= lastWindowsDelta;
        assert(lastWindowsDelta == y);
    }
}
@end

static void Send(WineApplicationController *controller, WineWindow *window,
                 double delta, double time, NSEventPhase phase, NSEventPhase momentum,
                 BOOL precise, NSEventModifierFlags modifiers) {
    HarnessScrollEvent *event = [[HarnessScrollEvent alloc]
        initWithDelta:delta time:time window:window];
    event.phase = phase;
    event.momentumPhase = momentum;
    event.hasPreciseScrollingDeltas = precise;
    event.modifierFlags = modifiers;
    double horizontal = nextHorizontalDelta;
    nextHorizontalDelta = 0;
    event.scrollingDeltaX = horizontal;
    CGEventSetDoubleValueField(event.CGEvent, kCGScrollWheelEventPointDeltaAxis2, horizontal);
    // CG's point-delta fields may quantize fractional values independently of
    // NSEvent's precise scrolling deltas; compare the actual stored originals.
    double originalY = CGEventGetDoubleValueField(event.CGEvent, kCGScrollWheelEventPointDeltaAxis1);
    double originalX = CGEventGetDoubleValueField(event.CGEvent, kCGScrollWheelEventPointDeltaAxis2);
    inputEvent = (NSEvent *)event;
    [controller handleScrollWheel:inputEvent];
    // Normalization must not mutate the user's incoming CG event.
    assert(CGEventGetDoubleValueField(event.CGEvent,
                                     kCGScrollWheelEventPointDeltaAxis1) == originalY);
    assert(CGEventGetDoubleValueField(event.CGEvent,
                                     kCGScrollWheelEventPointDeltaAxis2) == originalX);
    inputEvent = nil;
}

int main(void) {
    @autoreleasepool {
        assert(NSApp == nil);
        assert(!runStartupHookInstalled); // Run with SC4_TRACKPAD_ENABLED unset.
        WineApplication *application = [WineApplication new];
        WineWindow *window = [WineWindow new];
        window.title = @"SimCity 4";
        window.windowNumber = 101;
        application.keyWindow = window;
        application.isActive = YES;
        NSApp = (NSApplication *)application;
        WineApplicationController *controller = [WineApplicationController new];

        // Exercise the actual startup wrapper without creating NSApplication or
        // entering AppKit's event loop. Its original IMP is a counting no-op.
        Method realRunMethod = class_getInstanceMethod([NSApplication class], @selector(run));
        IMP realRun = method_getImplementation(realRunMethod);
        method_setImplementation(realRunMethod, (IMP)HarnessOriginalRun);
        assert(InstallRunStartupHook());
        assert(runStartupHookInstalled && !scrollHookInstalled);
        assert(InstallRunStartupHook());
        ((ApplicationRunHandler)method_getImplementation(realRunMethod))(application, @selector(run));
        assert(originalRunCalls == 1 && originalRunReceiver == application);
        assert(!runStartupHookInstalled && scrollHookInstalled);
        assert(method_getImplementation(realRunMethod) == (IMP)HarnessOriginalRun);
        method_setImplementation(realRunMethod, realRun);
        assert(NSApp == (NSApplication *)application);
        assert(InstallWhenWineIsReady());
        assert(scrollHookInstalled);
        assert(InstallScrollHook()); // Installation must remain idempotent.
        Send(controller, window, 0, 1.0, NSEventPhaseBegan, 0, YES, 0);
        nextHorizontalDelta = 0.25;
        Send(controller, window, 2, 1.1, NSEventPhaseChanged, 0, YES, 0);
        assert(normalizedCalls == 0);
        nextHorizontalDelta = 0.25;
        Send(controller, window, 2, 1.2, NSEventPhaseChanged, 0, YES, 0);
        assert(normalizedCalls == 1 && lastWindowsDelta == 120);
        Send(controller, window, 1000, 1.3, NSEventPhaseChanged, 0, YES, 0);
        Send(controller, window, -1000, 1.4, NSEventPhaseChanged, 0, YES, 0);
        Send(controller, window, 1000, 5.0, NSEventPhaseChanged, 0, YES, 0);
        Send(controller, window, 0, 5.1, NSEventPhaseEnded, 0, YES, 0);
        Send(controller, window, 1000, 5.2, 0, NSEventPhaseBegan, YES, 0);
        Send(controller, window, 1000, 5.3, 0, NSEventPhaseChanged, YES, 0);
        Send(controller, window, 0, 5.4, 0, NSEventPhaseEnded, YES, 0);
        assert(normalizedCalls == 1 && momentumSuppressed == 3);
        Send(controller, window, -10, 5.5, NSEventPhaseBegan, 0, YES, 0);
        assert(normalizedCalls == 2 && lastWindowsDelta == -120);
        Send(controller, window, 0, 5.6, NSEventPhaseCancelled, 0, YES, 0);
        Send(controller, window, 3, 5.7, NSEventPhaseBegan, 0, YES, 0);
        Send(controller, window, 0, 5.8, NSEventPhaseCancelled, 0, YES, 0);
        assert(normalizedCalls == 2);
        Send(controller, window, 4, 5.9, NSEventPhaseBegan, 0, YES, 0);
        assert(normalizedCalls == 3);

        // A plain mouse-wheel event retains its original identity and values.
        Send(controller, window, 300, 6.0, 0, 0, NO, 0);
        assert(passedThroughCalls == 1);
        Send(controller, window, 40, 6.1, NSEventPhaseBegan, 0, YES, NSEventModifierFlagShift);
        assert(passedThroughCalls == 2);
        application.isActive = NO;
        Send(controller, window, 40, 6.2, NSEventPhaseBegan, 0, YES, 0);
        assert(passedThroughCalls == 3);
        application.isActive = YES;
        WineWindow *other = [WineWindow new];
        other.title = @"SimCity 4";
        other.windowNumber = 202;
        Send(controller, other, 40, 6.3, NSEventPhaseBegan, 0, YES, 0);
        assert(passedThroughCalls == 4);
        window.title = @"Some other dialog";
        Send(controller, window, 40, 6.4, NSEventPhaseBegan, 0, YES, 0);
        assert(passedThroughCalls == 5);
        window.title = @"SimCity 4";
        Send(controller, window, 0, 6.5, NSEventPhaseBegan, 0, YES, 0);
        Send(controller, window, 0, 6.6, NSEventPhaseChanged, 0, YES, 0);
        Send(controller, window, 0, 6.7, NSEventPhaseEnded, 0, YES, 0);
        assert(normalizedCalls == 3); // Horizontal-only input does not zoom.

        // Cover the installed UsePreciseScrolling=N setting with old wheel debt.
        emulatePrecise = NO;
        debt = -87;
        Send(controller, window, 20, 7.0, NSEventPhaseBegan, 0, YES, 0);
        assert(normalizedCalls == 4 && lastWindowsDelta == 120);
        debt = 61;
        Send(controller, window, -20, 7.1, NSEventPhaseBegan, 0, YES, 0);
        assert(normalizedCalls == 5 && lastWindowsDelta == -120);
        assert(checkedWindowNumber == 101);

        // Horizontal intent stays horizontal despite later vertical drift;
        // its original events and momentum retain their identities and deltas.
        NSUInteger beforeHorizontal = passedThroughCalls;
        nextHorizontalDelta = 5;
        Send(controller, window, 0.5, 7.15, NSEventPhaseBegan, 0, YES, 0);
        nextHorizontalDelta = 10;
        Send(controller, window, 15, 7.16, NSEventPhaseChanged, 0, YES, 0);
        Send(controller, window, 0, 7.17, NSEventPhaseEnded, 0, YES, 0);
        nextHorizontalDelta = 100;
        Send(controller, window, 0.2, 7.18, 0, NSEventPhaseBegan, YES, 0);
        Send(controller, window, 0, 7.19, 0, NSEventPhaseEnded, YES, 0);
        assert(passedThroughCalls == beforeHorizontal + 5);
        assert(horizontalPassthrough == 5 && normalizedCalls == 5);

        // A new focused game window has an independent gesture state.
        application.keyWindow = other;
        Send(controller, other, 20, 7.2, NSEventPhaseChanged, 0, YES, 0);
        assert(normalizedCalls == 6 && checkedWindowNumber == 202);
        [[NSNotificationCenter defaultCenter] postNotificationName:
            NSApplicationDidResignActiveNotification object:application];
        assert(focusResets == 1 && !scrolling.hasEvent);
        [[NSNotificationCenter defaultCenter] postNotificationName:
            NSApplicationWillTerminateNotification object:application];
        assert(!scrollHookInstalled);
        NSUInteger beforeRestore = passedThroughCalls;
        Send(controller, other, 300, 8.0, NSEventPhaseBegan, 0, YES, 0);
        assert(passedThroughCalls == beforeRestore + 1); // Original implementation restored.
        if (terminationObserver) {
            [[NSNotificationCenter defaultCenter] removeObserver:terminationObserver];
            terminationObserver = nil;
        }
        NSApp = nil;
        puts("PASS: startup run-IMP hook/restoration/call-through without NSApp creation, actual production scroll swizzle, one step per phased vertical swipe, vertical momentum suppression, horizontal intent/momentum passthrough, original wheel/modifier/window passthrough, exact Win32 +/-120 with both Wine precision branches, focus reset, and unhook. No windows created or input posted.");
    }
    return 0;
}
