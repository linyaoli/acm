#include <stdio.h>

void makeN(int a[], int an, int b[], int bn) {

    int index[100] = {0};
    int i,j;
    int N = 10;
    for ( i = 0; i < an; i++)
        index[a[i]] = 1;
    for ( i = 0; i < bn; i++)
        if (b[i] <= N && index[(N-b[i])] == 1)
            printf("%d %d\n", N-b[i], b[i]);

}

int main( ) {

    int a[10] = {1,2,3,5,7,8,12,31,21,13};
    int b[7] = {3,4,5,6,7,8,9};

    makeN(a, 10, b, 7);

    return 0;
}
