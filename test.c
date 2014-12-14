#include<stdio.h>

void reverse(const char* str) {
  char c = ' ';
  int n = 0;
  while (c != '\0') {
    c = *(str++);
    n++;
  }
  n--;
  printf("%c", str);

}

int main() {

  reverse("abcdefg d");
  return 0;
}
