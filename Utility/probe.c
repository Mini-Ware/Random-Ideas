#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  char load[40];
  char msg[20];
  char address[20];
  unsigned int n;

  n = 0;

  for (unsigned int i=1; i<21; i++){
    strcpy(load, "ping -c 1 ");
    strcpy(msg, "192.168.x.");
    strcpy(address, "");

    sprintf(address, "%d", i);
    strcat(msg, address);

    strcat(load, msg);
    strcat(load, " > /dev/null");

    int status = system(load);

    if (i > 1){
      printf("\e[1A");
    }

    if (status == 0){
      printf("192.168.x.%d is connected\n", i);
      n = n+1;
    }

    printf("Progress: %d/255\n", i);
  }

  printf("%d device(s) detected!\n", n);
  return 0;

}
