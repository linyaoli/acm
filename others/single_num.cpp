#include <iostream>
//input {1,2,3,1,1,3,3}
//output 2
//
using namespace std;
int main(void) {

    int one = 0, two = 0;
    int a[7] = {1,2,3,1,1,3,3};
    for (int i = 0;i < 7; i++) {
        int one_ = (one^a[i]) & ~two;
        int two_ = (a[i] & one) | (~a[i] & two);
        one = one_;
        two = two_;
    }
    cout<<one;
    return 0;
}
