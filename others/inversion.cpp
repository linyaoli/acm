#include<iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

int main(){

    int a = 100;
    int i = 0;
    int aa;
    int k=0;
    while (a != 0) {
        aa = a%2;
        a = a>>1;
        k += (aa^1)*pow(2, i);
        i ++;
    }
    cout<<k<<endl;;
    return 0;
}
