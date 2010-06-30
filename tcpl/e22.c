#include <stdio.h>
#define N 10


void flod(char []);
void cls(char [],int);

main() {
  char line[N+1];
  flod(line);
}

void flod(char s[]) {
  int c,n;
  for(n = 0;(c = getchar())!=EOF;n++) {
    if (c == '\n') {
      if (n < N) {
        s[n+1] = '\0';
        printf("%s\n",s);
      }
      else if(n == N) {
        s[n] = '\0';
        printf("%s\n",s);
      }
      n = 0;
      cls(s,N);
    }
    else {
      if(n < N) {
      s[n] = c;
     }
    else {
      for (;s[n] == ' ' || s[n] == '\t';n--)
        s[n] = '\0';
      if (n == N)
        s[n] = '\0';
      printf("%c*\n",s[n-1]);
      printf("%s|\n",s);
      n = 0;
      cls(s,N);
      s[n] = c;
    }
  }
}
}
      

void cls(char s[],int t) {
  int i;
  for (i = 0;i<t;i++)
    s[i] = '\0';
}
