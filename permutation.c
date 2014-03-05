#include<stdio.h>
#include<string.h>

void swap(char* a, char* b) {
    char t = *a;
    *a = *b;
    *b = t;
}

void permutation (char* str, int i, int n) {
    int j = 0;
    if (i == n-1) {
        if(strlen(str) == n)
            printf("%s\n", str);
    }
    else
    for (j = i;j <= n; j++) {
        //swap
        swap(str+i, str+j);
        permutation(str, i+1, n);
        swap(str+i, str+j);
    }
}


int main(void) {

    char str[4] = "AaBb";
    permutation(str, 0, strlen(str));
    return 0;
}
