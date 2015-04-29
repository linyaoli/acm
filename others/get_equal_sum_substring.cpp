#include <iostream>

using namespace std;

int main() {


    string s = "986561517416921217551395112859219257312";
    string sasdd = "123231";
    string sasd = "121";
    string sa = "1221131";
    int len = s.length();

    int left = 0, right = 0;
    int max = 0;

    for (int i = 0; i < len - 1; i++) {
        left = 0;
        right = 0;
        for (int j = 0; j <= (i <= (len)/2?i:len-i-1); j++) {
            cout<<j;
            left += (int)(s[i-j] - '0');
            right += (int)(s[i+j+1]- '0');
            if (left == right) {
                if (max < j+1)
                    max = j+1;
            }
        }
        cout<<endl;
    }
    if (max == 0)
        cout<<1<<endl;
    else
        cout<<max*2<<endl;

    return 0;
}
