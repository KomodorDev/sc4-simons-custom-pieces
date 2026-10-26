#import <Cocoa/Cocoa.h>
@interface WineApplication : NSApplication
- (void)setWineController:(id)controller;
@end
@implementation WineApplication
- (void)setWineController:(id)controller { (void)controller; }
@end
@interface WineApplicationController : NSObject
- (void)handleScrollWheel:(NSEvent *)event;
@end
@implementation WineApplicationController
- (void)handleScrollWheel:(NSEvent *)event { (void)event; }
@end
int main(int argc, const char **argv) {
    (void)argc; (void)argv;
    @autoreleasepool {
        [WineApplication sharedApplication];
        [NSApp setActivationPolicy:NSApplicationActivationPolicyProhibited];
        [NSApp finishLaunching];
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 2.0, false);
        puts("Headless startup harness completed; no input posted.");
    }
    return 0;
}
