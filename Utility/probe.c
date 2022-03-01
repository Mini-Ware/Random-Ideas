#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  char load[30];
  char prefix[13];
  char address[4];
  unsigned int n;

  n = 0;

  for (unsigned int i=1; i<127; i++){
    strcpy(load, "ping -c 1 ");

    //Loop through IP addresses of private network
    strcpy(prefix, "192.168.18.");
    strcpy(address, "");

    sprintf(address, "%d", i);
    strcat(prefix, address);

    strcat(load, prefix);
    strcat(load, " > /dev/null");

    //Ping the IP address for response
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
