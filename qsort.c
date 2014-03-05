#include <stdio.h>


void setswap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void quick_sort(int s[], int l, int r) {

    if (l < r) {
        int i = l, j = r, x = s[l];
        while (i < j) {
            while (i < j && x <= s[j])
                j--;
            //setswap(&s[l], &s[j]);
            if (i < j)
                s[i++] = s[j];

            while (i < j && s[i] < x)
                i++;
            //setswap(&s[i], &s[j]);
            if (i < j)
                s[j--] = s[i];
        }

        s[i] = x;
        quick_sort(s, l, i-1);
        quick_sort(s, i+1, r);
    }
}

int main() {

    int a[10] = {72, 6, 57, 88, 60, 42, 83, 73, 48, 85};
    quick_sort(a, 0, 9);

    for (int i = 0;i < 10;i++)
        printf("%d ", a[i]);

    return 0;
}
