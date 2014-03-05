#include <stdio.h>

int check(int n) {

    if (n == 1 || n == 2)
        return 1;
    if (n%2 == 1)
        return 0;
    return check(n/2);
}

int main(void) {

    printf ("%d ", check(1024));
    return 0;
}
