#import <Cocoa/Cocoa.h>
#include <sys/file.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

static NSString *appPath, *iniPath, *batPath;

static void fail(NSString *message) {
    @throw [NSException exceptionWithName:@"DisplayModeError" reason:message userInfo:nil];
}

static NSString *runPS(NSString *field) {
    NSTask *task = [NSTask new];
    task.executableURL = [NSURL fileURLWithPath:@"/bin/ps"];
    task.arguments = @[@"-ww", @"-axo", [@"pid=," stringByAppendingString:field]];
    NSPipe *out = [NSPipe pipe];
    task.standardOutput = out;
    task.standardError = [NSPipe pipe];
    NSError *error = nil;
    if (![task launchAndReturnError:&error]) fail(@"I could not check whether SimCity 4 is running. Nothing was changed.");
    NSData *data = [out.fileHandleForReading readDataToEndOfFile];
    [task waitUntilExit];
    if (task.terminationStatus != 0) fail(@"I could not check whether SimCity 4 is running. Nothing was changed.");
    return [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
}

static NSDictionary *processes(NSString *field) {
    NSMutableDictionary *result = [NSMutableDictionary dictionary];
    NSRegularExpression *pattern = [NSRegularExpression regularExpressionWithPattern:@"^\\s*(\\d+)\\s+(.+)$" options:0 error:nil];
    for (NSString *line in [runPS(field) componentsSeparatedByString:@"\n"]) {
        NSTextCheckingResult *match = [pattern firstMatchInString:line options:0 range:NSMakeRange(0, line.length)];
        if (match) result[[line substringWithRange:[match rangeAtIndex:1]]] = [line substringWithRange:[match rangeAtIndex:2]];
    }
    return result;
}

static BOOL gameIsRunning(void) {
    NSDictionary *commands = processes(@"comm=");
    NSDictionary *arguments = processes(@"args=");
    NSString *launcher = [appPath stringByAppendingPathComponent:@"Contents/MacOS/wineskinlauncher"];
    NSString *wineRoot = [[appPath stringByAppendingPathComponent:@"Contents/SharedSupport/wine"] stringByAppendingString:@"/"];
    NSSet *wineNames = [NSSet setWithArray:@[@"wine", @"wine64", @"wine32on64", @"wine-preloader", @"wine64-preloader", @"wine32on64-preloader"]];
    for (NSString *pid in commands) {
        NSString *executable = [commands[pid] stringByStandardizingPath];
        if ([executable isEqualToString:launcher]) return YES;
        if ([executable hasPrefix:wineRoot] && [wineNames containsObject:executable.lastPathComponent]) {
            NSString *args = arguments[pid];
            // Examine only genuine Wine processes from this app, never a shell's command text.
            if (args && [args rangeOfString:@"SimCity 4.exe" options:NSCaseInsensitiveSearch].location != NSNotFound) return YES;
        }
    }
    return NO;
}

static void requireStopped(void) {
    if (gameIsRunning()) fail(@"SimCity 4 is still open or starting.\n\nSave your city, quit SimCity 4 completely, and then open this helper again. Nothing was changed.");
}

static NSData *readFile(NSString *path) {
    NSError *error = nil;
    NSData *data = [NSData dataWithContentsOfFile:path options:0 error:&error];
    if (!data) fail([NSString stringWithFormat:@"I could not read %@. Nothing was changed.", path.lastPathComponent]);
    return data;
}

static NSString *setting(NSString *text, NSString *key, NSRange *valueRange) {
    NSString *pattern = [NSString stringWithFormat:@"(?m)^[ \\t]*%@[ \\t]*=[ \\t]*([^;\\r\\n]*?)[ \\t]*(?:;[^\\r\\n]*)?\\r?$", [NSRegularExpression escapedPatternForString:key]];
    NSRegularExpression *regex = [NSRegularExpression regularExpressionWithPattern:pattern options:0 error:nil];
    NSArray *matches = [regex matchesInString:text options:0 range:NSMakeRange(0, text.length)];
    if (matches.count != 1) fail([NSString stringWithFormat:@"The graphics settings contain a missing or repeated %@ value. Nothing was changed.", key]);
    NSRange range = [matches[0] rangeAtIndex:1];
    if (valueRange) *valueRange = range;
    return [text substringWithRange:range];
}

static NSArray<NSData *> *prepareChanges(NSData *ini, NSData *bat, BOOL fullscreen) {
    // Latin-1 maps every byte directly, preserving comments, whitespace and line endings.
    NSString *iniText = [[NSString alloc] initWithData:ini encoding:NSISOLatin1StringEncoding];
    NSString *batText = [[NSString alloc] initWithData:bat encoding:NSISOLatin1StringEncoding];
    NSDictionary *required = @{@"WindowWidth": @"1920", @"WindowHeight": @"1200", @"ColorDepth": @"32", @"Driver": @"DirectX", @"ForceDrawOnScroll": @"true", @"Enabled": @"true"};
    for (NSString *key in required) {
        if ([setting(iniText, key, NULL) caseInsensitiveCompare:required[key]] != NSOrderedSame)
            fail(@"The game settings have changed since this helper was prepared. It requires DirectX, 1920 × 1200, 32-bit colour and full redraw enabled. Nothing was changed.");
    }
    NSRange modeRange;
    NSString *oldMode = setting(iniText, @"WindowMode", &modeRange);
    if (![@[@"Windowed", @"FullScreen"] containsObject:oldMode]) fail(@"The current window mode is not recognised. Nothing was changed.");
    NSRegularExpression *commandPattern = [NSRegularExpression regularExpressionWithPattern:@"(?m)^[ \\t]*\"SimCity 4\\.exe\"[ \\t]+[^\\r\\n]+" options:0 error:nil];
    NSArray *commands = [commandPattern matchesInString:batText options:0 range:NSMakeRange(0, batText.length)];
    if (commands.count != 1) fail(@"The game's launcher has changed. I could not identify exactly one SimCity 4 command. Nothing was changed.");
    NSRange commandRange = [commands[0] range];
    NSString *command = [batText substringWithRange:commandRange];
    NSRegularExpression *flagPattern = [NSRegularExpression regularExpressionWithPattern:@"(?<!\\S)-(w|f)(?!\\S)" options:0 error:nil];
    NSArray *flags = [flagPattern matchesInString:command options:0 range:NSMakeRange(0, command.length)];
    if (flags.count != 1 || [command rangeOfString:@" -r1920x1200x32"].location == NSNotFound || [command rangeOfString:@" -d:DirectX"].location == NSNotFound)
        fail(@"The game's launcher does not match the expected display settings. Nothing was changed.");
    NSRange flagRange = [flags[0] range];
    NSString *oldFlag = [command substringWithRange:flagRange];
    if (![[oldMode isEqualToString:@"FullScreen"] ? @"-f" : @"-w" isEqualToString:oldFlag])
        fail(@"The launcher and graphics settings disagree. Nothing was changed.");
    flagRange.location += commandRange.location;
    NSString *newINI = [iniText stringByReplacingCharactersInRange:modeRange withString:fullscreen ? @"FullScreen" : @"Windowed"];
    NSString *newBAT = [batText stringByReplacingCharactersInRange:flagRange withString:fullscreen ? @"-f" : @"-w"];
    return @[[newINI dataUsingEncoding:NSISOLatin1StringEncoding], [newBAT dataUsingEncoding:NSISOLatin1StringEncoding]];
}

static NSString *stageData(NSString *target, NSData *data) {
    struct stat info;
    if (lstat(target.fileSystemRepresentation, &info) != 0 || !S_ISREG(info.st_mode)) fail(@"An expected settings file is missing or is not a regular file. Nothing was changed.");
    NSString *template = [target stringByAppendingString:@".display-mode-XXXXXX"];
    char *path = strdup(template.fileSystemRepresentation);
    int fd = mkstemp(path);
    if (fd < 0) { free(path); fail(@"I could not prepare the settings change. Nothing was changed."); }
    NSString *temporary = [[NSFileManager defaultManager] stringWithFileSystemRepresentation:path length:strlen(path)];
    free(path);
    const unsigned char *bytes = data.bytes;
    NSUInteger remaining = data.length;
    BOOL ok = fchmod(fd, info.st_mode & 07777) == 0;
    while (ok && remaining) {
        ssize_t count = write(fd, bytes, remaining);
        if (count < 0 && errno == EINTR) continue;
        if (count <= 0) { ok = NO; break; }
        bytes += count;
        remaining -= count;
    }
    if (ok) ok = fsync(fd) == 0;
    if (close(fd) != 0) ok = NO;
    if (!ok) { unlink(temporary.fileSystemRepresentation); fail(@"I could not prepare the settings change. Nothing was changed."); }
    return temporary;
}

static void applyChanges(NSData *oldINI, NSData *oldBAT, NSArray<NSData *> *newData) {
    NSMutableArray<NSString *> *temporary = [NSMutableArray array];
    @try {
        NSString *nextINI = stageData(iniPath, newData[0]); [temporary addObject:nextINI];
        NSString *nextBAT = stageData(batPath, newData[1]); [temporary addObject:nextBAT];
        NSString *undoINI = stageData(iniPath, oldINI); [temporary addObject:undoINI];
        requireStopped();
        if (![readFile(iniPath) isEqual:oldINI] || ![readFile(batPath) isEqual:oldBAT]) fail(@"The settings changed while this helper was open. Please open it again. Nothing was changed.");
        if (rename(nextINI.fileSystemRepresentation, iniPath.fileSystemRepresentation) != 0) fail(@"I could not save the graphics setting. Nothing was changed.");
        if (rename(nextBAT.fileSystemRepresentation, batPath.fileSystemRepresentation) != 0) {
            if (rename(undoINI.fileSystemRepresentation, iniPath.fileSystemRepresentation) != 0) {
                [temporary removeObject:undoINI];
                fail([NSString stringWithFormat:@"The launcher update failed, and the previous graphics setting could not be restored. Do not launch the game yet. The original graphics file is saved at:\n%@", undoINI]);
            }
            fail(@"I could not save the launcher setting. The previous graphics setting was restored; the game settings are unchanged.");
        }
    } @finally {
        for (NSString *path in temporary) unlink(path.fileSystemRepresentation);
    }
}

static void notice(NSString *title, NSString *message) {
    NSAlert *alert = [NSAlert new];
    alert.messageText = title;
    alert.informativeText = message;
    [alert addButtonWithTitle:@"OK"];
    [alert runModal];
}

int main(int argc, const char *argv[]) {
    @autoreleasepool {
        appPath = [NSHomeDirectory() stringByAppendingPathComponent:@"Applications/SimCity 4 Windows.app"];
        iniPath = [NSHomeDirectory() stringByAppendingPathComponent:@"Documents/SimCity 4 Windows/Plugins/SC4GraphicsOptions.ini"];
        batPath = [appPath stringByAppendingPathComponent:@"Contents/SharedSupport/prefix/drive_c/launch-sc4.bat"];
        BOOL dryRun = argc == 3 && strcmp(argv[1], "--dry-run") == 0;
        int lockFD = -1;
        if (!dryRun) {
            [NSApplication sharedApplication];
            [NSApp setActivationPolicy:NSApplicationActivationPolicyRegular];
            [NSApp activateIgnoringOtherApps:YES];
        }
        @try {
            NSData *oldINI = readFile(iniPath), *oldBAT = readFile(batPath);
            BOOL fullscreen;
            if (dryRun) {
                if (strcmp(argv[2], "fullscreen") && strcmp(argv[2], "windowed")) fail(@"Use --dry-run fullscreen or --dry-run windowed.");
                fullscreen = strcmp(argv[2], "fullscreen") == 0;
            } else {
                NSString *lockPath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"SimCity4-display-mode.lock"];
                lockFD = open(lockPath.fileSystemRepresentation, O_CREAT | O_RDWR, 0600);
                if (lockFD < 0 || flock(lockFD, LOCK_EX | LOCK_NB) != 0) fail(@"Another display-mode helper is already open. Close it first. Nothing was changed.");
                requireStopped();
                NSAlert *choice = [NSAlert new];
                choice.messageText = @"How would you like to play SimCity 4?";
                choice.informativeText = @"Built-in Full Screen fills your main display. You cannot drag the game to another monitor in this mode.\n\nMovable Window lets you drag the game to your 4K monitor. It keeps the older Windows-style border needed for correct clicks.\n\nBoth use 1920 × 1200. The game will stay closed until you open it yourself.";
                [choice addButtonWithTitle:@"Built-in Full Screen"];
                [choice addButtonWithTitle:@"Movable Window"];
                [choice addButtonWithTitle:@"Cancel"].keyEquivalent = @"\033";
                NSModalResponse answer = [choice runModal];
                if (answer == NSAlertThirdButtonReturn) return 0;
                fullscreen = answer == NSAlertFirstButtonReturn;
            }
            NSArray *newData = prepareChanges(oldINI, oldBAT, fullscreen);
            if (dryRun) {
                printf("Validated %s: INI %lu -> %lu bytes; launcher %lu -> %lu bytes.\nGame/launcher running: %s. No files changed.\n", fullscreen ? "FullScreen" : "Windowed", (unsigned long)oldINI.length, (unsigned long)[newData[0] length], (unsigned long)oldBAT.length, (unsigned long)[newData[1] length], gameIsRunning() ? "yes (a real change would be refused)" : "no");
                return 0;
            }
            applyChanges(oldINI, oldBAT, newData);
            notice(@"Display mode saved", [NSString stringWithFormat:@"%@ is selected.\n\nDouble-click your usual SimCity 4 Windows icon to start the game.\n\nTo change modes later, save your city and quit the game, then open this helper again.", fullscreen ? @"Built-in Full Screen" : @"Movable Window"]);
        } @catch (NSException *error) {
            if (dryRun) fprintf(stderr, "%s\n", error.reason.UTF8String);
            else notice(@"Display mode was not changed", error.reason);
            return 1;
        } @finally {
            if (lockFD >= 0) close(lockFD);
        }
    }
    return 0;
}
