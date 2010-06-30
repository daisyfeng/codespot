#include <stdio.h>

void tabstop(int,int);
int totab(int);

main() {
  int c,p,nb,last;
  
  p = 0;
  nb = 0;
  while((c=getchar()) != EOF) {
    if(c == ' ') {
      last = c;
      ++nb;
      ++p;
    }
    else if (c != ' ' && c != '\n') {
        if(last == ' ') {           
           tabstop(p,nb);
           nb = 0; 
        }
        putchar(c);
        ++p;
        last = c;
      }
    else {
      putchar(c);
      p = 0;
      nb = 0;
    }
    
  }
}

void tabstop(int p,int nb) {
  int first,i;
  first = p-nb;
  while (nb > 0) {
    if (nb < 4) {
      for(;nb > 0;nb--)
        putchar('_');
    }
    else {
      i = totab(first);
      first += i;
      nb -= i;
    }
  }
}  

int totab(int p){
  int i,j;
  i = 4-p%4;
  j = i;
  if(i<4) {
    while(i) {
      putchar('_');
      i--;
    }
  }
  else 
    printf("\\t");
  return j ;  
}


