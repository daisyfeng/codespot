#include<stdio.h>


main () {
  int c,state;
  int nw = 0;
  int str[1000];

  while((c = getchar()) != EOF) {
    if (c!=' ' && c!='\t' && c!='\n') {
      str[nw] = c;
      ++nw;
      state = 1;
    }
    else if (state == 1) {
      for (int i = 0;i<=nw;i++)
	putchar(str[i]);
      printf("\t");
      while(nw >= 0) {
	putchar('#');
	nw--;
      }
      printf("\n");
      state = 0;
    }
  }
}
      
