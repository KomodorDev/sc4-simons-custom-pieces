#import <Cocoa/Cocoa.h>
#include <libproc.h>
static BOOL IsHelper(NSRunningApplication *app) {
    char executable[PROC_PIDPATHINFO_MAXSIZE];
    return app && proc_pidpath(app.processIdentifier, executable, sizeof(executable)) > 0 &&
        strcmp(executable, "/Users/simonhinterreiter/Applications/SimCity Trackpad Zoom.app/Contents/MacOS/SC4ScrollHelper") == 0;
}
int main(void) {
    @autoreleasepool {
        NSArray *apps=[NSRunningApplication runningApplicationsWithBundleIdentifier:@"local.simon.simcity-trackpad-zoom"];
        BOOL found=NO, allHidden=YES;
        for(NSRunningApplication *app in apps) {
            if(!IsHelper(app)) continue;
            found=YES;
            BOOL before=app.hidden, success=[app hide];
            CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.5, false);
            BOOL after=app.hidden;
            NSDictionary *result=@{@"pid":@(app.processIdentifier),@"hidden_before":@(before),
                @"hide_returned":@(success),@"hidden_after":@(after),@"active":@(app.active)};
            NSData *json=[NSJSONSerialization dataWithJSONObject:result options:0 error:NULL];
            puts([[NSString alloc] initWithData:json encoding:NSUTF8StringEncoding].UTF8String);
            allHidden &= success && after;
        }
        return found && allHidden ? 0 : 1;
    }
}
