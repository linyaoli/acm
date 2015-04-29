#include <math.h>
#include <iostream>

using namespace std;

void subsets(char* set, int set_size) {

    unsigned int _size = pow(2, set_size);
    int counter, j;

    for (counter = 0; counter < _size; counter++) {
        for (j = 0; j < _size; j++) {
            if (counter & (1 << j))
                cout<<set[j]<<" ";
        }
        cout<<endl;
    }
}

int main() {
    char set[] = {'a', 'b', 'c', 'd'};
    subsets(set, 4);

    return 0;
}
