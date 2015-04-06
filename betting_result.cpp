#include <iostream>
using namespace std;

int main() {

    int init = 15;
    string bet = "LLLWLLLL";//8

    int len = bet.length();
    int rod = 1;
    for (int i = 0; i < len; i++) {
        if ('W' == bet[i]) {
            init += rod;
            rod = 1;
        }
        else if ('L' == bet[i]) {
            init -= rod;
            rod *= 2;
        }
        else {

        }

    }
    cout<<init<<endl;

    return 0;
}
