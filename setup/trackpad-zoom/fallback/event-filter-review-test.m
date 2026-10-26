// Independent pure data-plane tests. The TEST switch excludes all app/tap code.
#define SC4_SCROLL_HELPER_TEST
#define main IncludedOriginalTestMain
#include "SC4ScrollHelper.m"
#undef main

static CGEventRef EventXY(int x, int y, int phase, int momentum, double time) {
    CGEventRef e = TestEvent(y, phase, momentum, time);
    CGEventSetIntegerValueField(e, kCGScrollWheelEventPointDeltaAxis2, x);
    return e;
}
static void Check(CGEventRef e, BOOL passed, int expectedPointY) {
    CGEventRef result = FilterScroll(e);
    assert((result != NULL) == passed);
    if (passed) {
        assert(result == e);
        assert(CGEventGetDoubleValueField(e, kCGScrollWheelEventPointDeltaAxis1) == expectedPointY);
    }
    CFRelease(e);
}
int main(void) {
    @autoreleasepool {
        assert(NSApp == nil);
        ResetSwipe();
        Check(EventXY(0, 1, kCGScrollPhaseBegan, 0, 1), NO, 0);
        Check(EventXY(1, 2, kCGScrollPhaseChanged, 0, 1.1), NO, 0);
        CGEventRef step = EventXY(0, 1, kCGScrollPhaseChanged, 0, 1.2);
        CGEventSetLocation(step, CGPointMake(123, 456));
        uint64_t timestamp = CGEventGetTimestamp(step);
        assert(FilterScroll(step) == step);
        assert(CGEventGetDoubleValueField(step, kCGScrollWheelEventPointDeltaAxis1) * 6 == 120);
        assert(CGEventGetDoubleValueField(step, kCGScrollWheelEventPointDeltaAxis2) == 0);
        assert(CGPointEqualToPoint(CGEventGetLocation(step), CGPointMake(123, 456)));
        assert(CGEventGetTimestamp(step) == timestamp);
        assert(CGEventGetFlags(step) == 0);
        CFRelease(step);
        Check(EventXY(100, -500, kCGScrollPhaseChanged, 0, 5), NO, 0);
        Check(EventXY(0, 0, kCGScrollPhaseEnded, 0, 5.1), NO, 0);
        Check(EventXY(0, 500, 0, kCGMomentumScrollPhaseBegin, 5.2), NO, 0);
        Check(EventXY(0, -4, kCGScrollPhaseBegan, 0, 6), YES, -20);
        Check(EventXY(0, 20, kCGScrollPhaseCancelled, 0, 6.1), NO, 0);
        Check(EventXY(0, 4, kCGScrollPhaseBegan, 0, 6.2), YES, 20);

        ResetSwipe();
        Check(EventXY(0, 4, 0, 0, 10), YES, 20);
        Check(EventXY(0, 100, 0, 0, 10.1), NO, 0);
        Check(EventXY(0, -4, 0, 0, 10.8), YES, -20);

        ResetSwipe();
        Check(EventXY(2, 0, kCGScrollPhaseBegan, 0, 20), NO, 0);
        Check(EventXY(2, 1, kCGScrollPhaseChanged, 0, 20.1), YES, 1);
        Check(EventXY(1, 100, kCGScrollPhaseChanged, 0, 20.2), YES, 100);
        Check(EventXY(0, 0, kCGScrollPhaseEnded, 0, 20.3), YES, 0);
        Check(EventXY(12, 8, 0, kCGMomentumScrollPhaseContinue, 20.4), YES, 8);

        CGEventRef wheel = CGEventCreateScrollWheelEvent(NULL, kCGScrollEventUnitLine, 1, 3);
        double before = CGEventGetDoubleValueField(wheel, kCGScrollWheelEventPointDeltaAxis1);
        assert(FilterScroll(wheel) == wheel);
        assert(CGEventGetDoubleValueField(wheel, kCGScrollWheelEventPointDeltaAxis1) == before);
        CFRelease(wheel);
        CGEventRef modified = EventXY(0, 200, kCGScrollPhaseBegan, 0, 30);
        CGEventSetFlags(modified, kCGEventFlagMaskShift);
        Check(modified, YES, 200);
        assert(NSApp == nil);
        puts("PASS: independent CG filter threshold, exact Wine delta, phase/gap/cancel, horizontal/momentum, mouse/modifier, and preservation tests. No application, tap, permission check, or posted input.");
    }
    return 0;
}
