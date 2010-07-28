#include <stdio.h>
#include <string.h>

void itob(int,char [],int);

void itob(int n,char s[],int b) {
  int k,m,j;
  char p[20];
  k = 0;
  do {
    p[k++] = (n%b < 9)?(n%b + '0'):(n%b + 'a' -10) ;
  }
  while((n /= b) >= b);
  p[k++] = (n<9)?(n+'0'):(n+'a'-10),p[k] = '\0';

  for (j=0,m = strlen(p) -1 ;m >= 0;m--)
    s[j++] = p[m];
  s[j] = '\0';
}

main ()
{
  char s[20];
  itob(30,s,16);
  printf("%s\n",s);
    
}
