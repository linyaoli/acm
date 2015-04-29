#include <stdio.h>
#include <stdlib.h>

int constChars(const char str[]) {
    int size = sizeof(str)/sizeof(char);
    printf("Size is %d.\n", size);
    int i = 0;
    for (i=0;i<size;i++)
       printf("%c ", str[i]);

    return 0;
}


int main(void) {

    char a[10]={'b','c','d','e','f','f','f','f','f','f'};
    constChars(a);
    return 0;

}
