#import <Cocoa/Cocoa.h>
#import <CoreGraphics/CoreGraphics.h>
NSDictionary* rect(CGRect r){return @{ @"x":@(r.origin.x),@"y":@(r.origin.y),@"width":@(r.size.width),@"height":@(r.size.height)};}
int main(){@autoreleasepool{
 NSMutableArray* screens=[NSMutableArray array];
 for(NSScreen* s in [NSScreen screens]){
  CGDirectDisplayID i=[[s.deviceDescription objectForKey:@"NSScreenNumber"] unsignedIntValue];
  [screens addObject:@{@"name":s.localizedName,@"id":@(i),@"appkitFrame":rect(s.frame),@"visibleFrame":rect(s.visibleFrame),@"backingScale":@(s.backingScaleFactor),@"cgBounds":rect(CGDisplayBounds(i))}];
 }
 NSMutableArray* windows=[NSMutableArray array];
 NSArray* all=(__bridge_transfer NSArray*)CGWindowListCopyWindowInfo(kCGWindowListOptionAll,kCGNullWindowID);
 for(NSDictionary* w in all){
  NSString* owner=[w objectForKey:(id)kCGWindowOwnerName]?:@"";
  NSString* name=[w objectForKey:(id)kCGWindowName]?:@"";
  if([owner.lowercaseString containsString:@"wine"]||[name.lowercaseString containsString:@"simcity"]||[owner.lowercaseString containsString:@"simcity"]){[windows addObject:w];}
 }
 NSDictionary* result=@{@"screens":screens,@"gameWindows":windows};
 NSData* data=[NSJSONSerialization dataWithJSONObject:result options:NSJSONWritingPrettyPrinted|NSJSONWritingSortedKeys error:nil];
 puts([[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding].UTF8String);
}}
