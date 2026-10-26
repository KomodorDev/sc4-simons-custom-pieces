#include <crt_externs.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
__attribute__((constructor)) static void probe(void) {
 char file[1024], result[512];
 const char *flag=getenv("SC4_TRACKPAD_ENABLED");
 const char *status=getenv("SC4_TRACKPAD_STATUS");
 int argc=*_NSGetArgc();
 int n=snprintf(file,sizeof(file),"/Users/simonhinterreiter/Documents/ChatGPT/Project_Sim_City/setup/trackpad-zoom/probe-%ld.json",(long)getpid());
 if(n<=0 || n>=sizeof(file))return;
 n=snprintf(result,sizeof(result),"{\"pid\":%ld,\"ppid\":%ld,\"argc\":%d,\"enabled_present\":%s,\"enabled_is_one\":%s,\"status_present\":%s}\n",(long)getpid(),(long)getppid(),argc,flag?"true":"false",flag&&!strcmp(flag,"1")?"true":"false",status?"true":"false");
 int fd=open(file,O_WRONLY|O_CREAT|O_TRUNC,0600);
 if(fd>=0){write(fd,result,(size_t)n);close(fd);}
}
