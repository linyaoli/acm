#include<stdio.h>

void findPrime(){
    int a[3000] = {0};
    int n = 3000;
    int i,j = 0;
    int k = 1;
    a[0] = 1;
    for (i = 1; i < n; i++){
        for(j = i; j < n; j++){
            k = (i+1)*(j+1);
            if (k <= n)
                a[k] = 1;
            else
                break;
        }
        k = 1;
    }
    for (i = 0; i < n; i++)
        if (a[i] == 0)
            printf("%d ", i);
}

int main(void){

    findPrime();
    return 0;
}
