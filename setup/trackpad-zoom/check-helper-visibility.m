#import <Cocoa/Cocoa.h>
#include <stdlib.h>
int main(int argc, const char **argv) {
    @autoreleasepool {
        if (argc!=2) return 2;
        pid_t pid=(pid_t)atoi(argv[1]);
        NSRunningApplication *app=[NSRunningApplication runningApplicationWithProcessIdentifier:pid];
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.5, false);
        NSMutableArray *windows=[NSMutableArray array];
        NSArray *all=CFBridgingRelease(CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements,kCGNullWindowID));
        for(NSDictionary *w in all) if([w[(id)kCGWindowOwnerPID] intValue]==pid)
            [windows addObject:@{@"onscreen":@YES,
                                 @"bounds":w[(id)kCGWindowBounds] ?: @{},
                                 @"window_id":w[(id)kCGWindowNumber] ?: @0}];
        NSDictionary *result=@{@"pid":@(pid),@"running":@(app && !app.terminated),
                              @"hidden":@(app.hidden),@"active":@(app.active),@"windows":windows};
        NSData *json=[NSJSONSerialization dataWithJSONObject:result options:0 error:NULL];
        puts([[NSString alloc] initWithData:json encoding:NSUTF8StringEncoding].UTF8String);
    }
}
