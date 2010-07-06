#include <stdio.h>

int calc(char [],int);
int pow(int,int);

main() {
  int c,i;
  char str[1000];
  i = 0;
  while((c = getchar()) != EOF) {
    if (c == '\n') {
      printf("%d\n",calc(str,i));
      i = 0;
    }else {
      str[i] = c;
      ++i;
    }
    
  }
}

int calc(char str[],int n) {
  int value = 0;
  int i = 0;
  if (str[0] == '0' && str[1] == 'x' || str[1] == 'X')
    i = 2;
  for(;i < n;i++) {

    if (str[i] >= '0' && str[i] <= '9')
      value += (str[i] - '0')*pow(16,n-i-1);
    else if(str[i] >= 'a' && str[i] <= 'f')
      value += ((str[i] - 'a') + 10)*pow(16,n-i-1);
    else if(str[i] >= 'A' && str[i] <= 'F')
      value += ((str[i] - 'A') + 10)*pow(16,n-i-1);
  }
  return value;
}

int pow(int x,int y) {
   if(y == 0) 
     return 1;
   else
     return x*pow(x,--y);
}
    
