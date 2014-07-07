#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int isNegative = 0;

double power(int a, int n) {

    if (n==0)
        return 1;
    if (n<0) {
        n = -n;
        isNegative = 1;
    }
    int i = 0;
    int result = 1;
    for (i= 0; i < n; i++) {
        result *= a;
    }
    if (isNegative == 1)
        return  1.0/result;
    else
        return result;
}

int main(void) {

    printf("%lf", power(2,10));
    return 0;
}
