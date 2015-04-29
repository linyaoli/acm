#include <iostream>
using namespace std;

int main(void) {

    int rating[7] = {4,2,3,1,7,6,5};
    int given[7] = {1, 1, 1, 1, 1, 1, 1};//at least one each
    for (int i = 0; i < 7; i++) {
        //greedy
        if (i == 0 && rating[i] > rating[i+1])
            given[i] += 1;
        else if (i == 6 && rating[i] > rating[i-1])
            given[i] += 1;
        else {
            if (rating[i] < rating[i-1] && given[i] >= given[i-1]) {
                given[i-1] += 1;
                for(int j = i; i > 0; i--) {
                    if (rating[j] < rating[j-1] && given[j] >= given[j-1])
                        given[j-1] += 1;
                }
            }
        }
    }
    for (int i = 0;i < 7; i++)
        cout<<given[i]<<endl;

    return 0;
}
