#include <iostream>
#include <math.h>
using namespace std;


int getsingle(int n) {

    if (n < 10) return 0;
    int nn = 1;
    while (n > 0 ) {
        nn *= n%10;
        n = n/10;
    }
    return 1+getsingle(nn);
}


int main() {

    cout<<getsingle(99);
    return 0;
}
