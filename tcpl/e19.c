#include <stdio.h>
#define MAXLINE 1000

int reverse(char []);

main () {
  char s[MAXLINE];

  while (reverse(s))
    printf("%s\n",s);
}

int reverse(char s[]) {
  int c,p,i;
  char tmp[MAXLINE];
  p = 0;
  while( (c = getchar()) != EOF && c != '\n' && p < MAXLINE) 
    tmp[p++] = c;
    p--;
    for(i=0;p>=0;)
      s[i++] = tmp[p--];
  
  s[i] = '\0';
  return 1;
}
    
