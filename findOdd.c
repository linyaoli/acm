#include <stdio.h>

int main() {

    int a[11] = {1,2,1,2,3,6,3,6,6,7,6};

    int i =0;
    for (i = 1;i < 11 ; i++)
        a[0] ^= a[i];

    printf("%d\n", a[0]);

    return 0;
}
