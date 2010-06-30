#include<stdio.h>

main() {
  float c;
  printf("%s\t%s\n","Fahrenheit","Celsius");
  for (float i=300.0;i>=0.0;i-=20) {
    c = 5.0/9.0*(i-32);
    printf("%10.1f\t%7.2f\n",i,c);
  }
  
  /* while implement */
  /* while (i<=300) { */
  /*   c = 5*(i-32)/9; */
  /*   printf("%d\t%d\n",i,c); */
  /*   i += 20; */
  /* } */
  /* do { */
  /*   c = 5*(i-32)/9; */
  /*   printf("%d\t%d\n",i,c); */
  /*   i += 20; */
  /* } while (i<=300); */
}
