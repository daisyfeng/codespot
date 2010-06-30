#include <stdio.h>

int check(int,char[]);

int finda(int,char[])

int checksquezz(int,char[]);

int cmp(char[]);

main() {
  char character[1000];
  int c;
  
  while((c = getchar()) != EOF) {
    check(c,character);
  }
  if(!cmp[character])
    printf("error\n");
}

int check(int c,char s[]) {
  int p,f;
  p = 0;
  
  if (c == '(' || c == '{' || c == '[' )
    s[p++] = c;
  else if (c == ')' || c == '}' || c == ']' ) {
    if (!finda(c,s))
      printf("%d character %c error\n",p,c);
  }
  else if (c == '/') {
    if ((c = getchar()) == '*') {
      s[p++] = '/';
      s[p++] = c;
      check(c);
    }
  }
  else if (c == '*') {
    if ((c = getchar()) == '/') {
      if(!findb(c,s))
        printf("%d character %c error\n",p,c);
    }
  }
}

