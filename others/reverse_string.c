#include<stdio.h>

void reverse(char* str) {
  char* start = str;
  char* end = str;
  while (*str) {
    end = str;
    str++;
  }
  str = start;
  char tc;
  while ( (end != start) && ((end - 1) != start) ){
    tc = *end;
    //FIXME
    //This assignment will cause bus error in linux env.
    //Most likely to be related with mem address initialization.
    //Works in windows tho.
    //*end = *start;
    //*start = tc;

    end--;
    start++;
  }
  printf("%s\n", str);
}

int main() {

  reverse("abcdefg d");
  return 0;
}
