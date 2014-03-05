#include <stdio.h>
#include <stdlib.h>

void findCommon(const char* a, int an, const char* b, int bn){

    int i,j = bn-1;
    int k = bn-1;
    for (i = bn-1; i < an; i++) {
        k = bn-1;
        if (a[i] == b[bn-1])
            for (j = i; j >= i - bn + 1; j--) {
                if (a[j] != b[k])
                    break;
                printf("%c", b[bn-1-k]);
                k--;
            }
        if (k<=0)
            printf("\n find it!");
    }

}

int main(void) {

    char* a = "abcijfghij klmn";
    char* b = "ghij kl";
    int an = 15;
    int bn = 7;
    findCommon(a, an, b, bn);
    return 0;
}
