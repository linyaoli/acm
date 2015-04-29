#include <stdio.h>
#define N 5

int a[N] = {0};

int climb(int n) {

    if (n >= N) return 1;
    int k;
    if (a[n] == 0) {
        k = climb(n+1) + climb(n+2);
        a[n] = k;
    }
    else
        k = a[n];

    return k;
}
int main(void) {

    printf("%d\n", climb(0));
    int i;
    for ( i = 0;i < N; i++)
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
