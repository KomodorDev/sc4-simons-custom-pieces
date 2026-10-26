#import <Cocoa/Cocoa.h>
#import <objc/runtime.h>
#import <assert.h>
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
        const char *originalPath=getenv("SC4_TRACKPAD_STATUS");
        assert(originalPath);
        char *savedPath=strdup(originalPath);
        unsetenv("SC4_TRACKPAD_STATUS");
        [WineApplication sharedApplication];
        [NSApp setActivationPolicy:NSApplicationActivationPolicyProhibited];
        [NSApp setWineController:[WineApplicationController new]];
        [NSTimer scheduledTimerWithTimeInterval:0.5 repeats:NO block:^(NSTimer *timer) {
            (void)timer;
            [NSApp stop:nil];
            NSEvent *wake = [NSEvent otherEventWithType:NSEventTypeApplicationDefined
                location:NSZeroPoint modifierFlags:0 timestamp:0 windowNumber:0
                context:nil subtype:0 data1:0 data2:0];
            [NSApp postEvent:wake atStart:NO];
        }];
        [NSApp run];
        const char *raw = savedPath;
        assert(raw);
        NSData *data=[NSData dataWithContentsOfFile:[NSString stringWithUTF8String:raw]];
        assert(data);
        NSDictionary *status=[NSJSONSerialization JSONObjectWithData:data options:0 error:NULL];
        assert([status[@"scroll_hook_installed"] boolValue]);
        assert([status[@"pid"] intValue]==getpid());
        free(savedPath);
        puts("PASS: late environment removed; helper constructor installed the scroll hook through real NSApplication run. No windows created; only an internal application wake event was queued.");
    }
    return 0;
}
