#import <ApplicationServices/ApplicationServices.h>
#include <stdio.h>
int main(){printf("accessibility=%d postEvents=%d\n",AXIsProcessTrusted(),CGPreflightPostEventAccess());return 0;}
