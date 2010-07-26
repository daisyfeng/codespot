#include <stdio.h>
#include <ctype.h>

void expand(char [],char []);

void expand(char s1[],char s2[]) {
  int i,j,n;
  for (i = 0,n = 0;s1[i] != '\0';i++) {
    if (isalpha(s1[i]) && s1[i+1] == '-' && isalpha(s1[i+2])) {
      for(j = 0;j <= s1[i+2] - s1[i];j++)
        s2[n++] = s1[i] + j;
      i +=2;
    }
    else if (isdigit(s1[i]) && s1[i+1] == '-' && isdigit(s1[i+2])) {
      for(j = 0;j <= s1[i+2] - s1[i];j++)
        s2[n++] = s1[i] + j;
      i +=2;
    }
    else if (s1[i] == '-' && ((isdigit(s1[i+1]) && isdigit(s2[n-1])) || (isalpha(s1[i+1]) && isalpha(s2[n-1])))) {
      for(j = 1;j < s1[i+1] - s2[n-1];j++)
        s2[n] = s2[n-1] + 1,n++;
      i ++;
    }
    else
      s2[n++] = s1[i];
  }
  s2[n] = '\0';
}

void expand1(char s1[], char s2[])
{
	int i, j, k, mov;
	for (i = j = 0; s1[i]; i++)
		if (s1[i] == '-' && i > 0 && s1[i - 1] != s1[i + 1] &&
		    ((s1[i - 1] >= '0' && s1[i - 1]<= '9' && s1[i + 1] >= '0' && s1[i + 1] <= '9') ||
			(s1[i - 1] >= 'a' && s1[i - 1]<= 'z' && s1[i + 1] >= 'a' && s1[i + 1] <= 'z') ||
		    (s1[i - 1] >= 'A' && s1[i - 1]<= 'Z' && s1[i + 1] >= 'A' && s1[i + 1] <= 'Z'))) {
			if (s1[i + 1] > s1[i - 1])
				mov = 1;
			else
				mov = -1;
			for (k = s1[i - 1] + mov; k != s1[i + 1]; k += mov)
				s2[j++] = k;
		}
		else
			s2[j++]=s1[i];
	s2[j] = 0;
}

main () {
  char s1[] = "A-C-zasdsadasoo0-9-b";
  char s2[100];
  expand(s1,s2);
  printf("%s\n",s2);
}
