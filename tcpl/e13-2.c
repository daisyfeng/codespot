#include<stdio.h>

main () {
  int nw,n,k;
  int p,c,max;
  int str[1000];
  
  for (n=0;n<1001;n++)
    str[n] = 0;
  nw = 0;
  max = 0;
  k = 0;
  while((c = getchar())!= 'E') {
    
    if(c != ' ' && c != '\t' && c != '\n') {
      putchar(c);
      p = c;
      str[nw]++;
    }
    else if (p != ' ' && p != '\t') {
      p = c;
      putchar(c);
      ++nw;
    }
    
  }
  printf("\n");
  for (int i = 0;i <= nw;i++) {
    if (max < str[i])
      max = str[i];
    printf("%d|",i);
  }
  printf("\n");
  for (int i = 0;i < max;i++) {
    printf("%d|",i);
    for (n = 0;n<nw;n++) {
      
      if (str[n] > i ) printf("*");
      else printf(" ");
      printf("|");
    }
    printf("\n");
  }  
}
