#include<stdio.h>
#define E EOF

main () {
  printf("%d",EOF);
  for (char c = getchar();c != E;c = getchar()) {
    putchar(c);
  }
}
