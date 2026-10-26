#import <Cocoa/Cocoa.h>
#include <libproc.h>

static NSString *const HelperPath = @"/Users/simonhinterreiter/Applications/SimCity Trackpad Zoom.app";
static NSString *const StatusPath = @"/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Trackpad Window status.json";

static BOOL IsHelper(NSRunningApplication *app) {
    char executable[PROC_PIDPATHINFO_MAXSIZE];
    return app && !app.terminated &&
        proc_pidpath(app.processIdentifier, executable, sizeof(executable)) > 0 &&
        strcmp(executable, "/Users/simonhinterreiter/Applications/SimCity Trackpad Zoom.app/Contents/MacOS/SC4ScrollHelper") == 0;
}

static NSInteger VisibleWindows(pid_t pid) {
    NSArray *windows = CFBridgingRelease(CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly | kCGWindowListExcludeDesktopElements, kCGNullWindowID));
    if (!windows) return -1;
    NSInteger count = 0;
    for (NSDictionary *window in windows) {
        CGRect bounds;
        if ([window[(id)kCGWindowOwnerPID] intValue] == pid &&
            [window[(id)kCGWindowLayer] intValue] == 0 &&
            [window[(id)kCGWindowAlpha] doubleValue] > 0 &&
            CGRectMakeWithDictionaryRepresentation((__bridge CFDictionaryRef)window[(id)kCGWindowBounds], &bounds) &&
            bounds.size.width > 0 && bounds.size.height > 0) ++count;
    }
    return count;
}

int main(void) {
    @autoreleasepool {
        __block NSRunningApplication *helper = nil;
        __block NSError *launchError = nil;
        __block BOOL completed = NO;
        NSWorkspaceOpenConfiguration *config = [NSWorkspaceOpenConfiguration configuration];
        config.arguments = @[@"--start"];
        config.activates = NO;
        config.hides = YES;
        config.createsNewApplicationInstance = NO;
        config.addsToRecentItems = NO;
        // Keep the run loop alive while launch completion arrives asynchronously.
        NSTimer *keepAlive = [NSTimer scheduledTimerWithTimeInterval:30 repeats:NO block:^(NSTimer *timer) {
            (void)timer;
        }];
        [[NSWorkspace sharedWorkspace] openApplicationAtURL:[NSURL fileURLWithPath:HelperPath]
            configuration:config completionHandler:^(NSRunningApplication *app, NSError *error) {
                dispatch_async(dispatch_get_main_queue(), ^{
                    helper = app;
                    launchError = error;
                    completed = YES;
                });
            }];

        double deadline = NSProcessInfo.processInfo.systemUptime + 10;
        double hiddenSince = 0;
        BOOL verified = NO;
        NSInteger visible = -1;
        while (NSProcessInfo.processInfo.systemUptime < deadline) {
            // NSRunningApplication refreshes changing properties on main-run-loop turns.
            CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.1, false);
            if (!completed) continue;
            if (launchError || !IsHelper(helper)) break;
            if (!helper.finishedLaunching) continue;
            if (!helper.hidden) {
                hiddenSince = 0;
                [helper hide];
                continue;
            }
            visible = VisibleWindows(helper.processIdentifier);
            if (visible != 0) { hiddenSince = 0; continue; }
            double now = NSProcessInfo.processInfo.systemUptime;
            if (!hiddenSince) hiddenSince = now;
            if (now - hiddenSince >= 0.8) { verified = YES; break; }
        }
        [keepAlive invalidate];
        NSDictionary *status = @{
            @"schema": @1, @"launcher_pid": @(getpid()), @"helper_pid": @(helper.processIdentifier),
            @"launch_finished": @(helper.finishedLaunching), @"hidden": @(helper.hidden),
            @"onscreen_helper_windows": @(visible), @"verified_hidden": @(verified),
            @"error": launchError.localizedDescription ?: @"",
            @"updated_unix_seconds": @([NSDate date].timeIntervalSince1970)
        };
        NSData *json = [NSJSONSerialization dataWithJSONObject:status options:0 error:NULL];
        [json writeToFile:StatusPath options:NSDataWritingAtomic error:NULL];
        puts([[NSString alloc] initWithData:json encoding:NSUTF8StringEncoding].UTF8String);
        return verified ? 0 : 1;
    }
}
