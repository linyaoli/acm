#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool checkPalindrome(string strIn) {
    string strInNew = "";
    for (string::iterator it=strIn.begin(); it != strIn.end(); ++it) {
        if ((*it >= 'a' && *it <= 'z'))
            strInNew += *it;
        else if (*it >= 'A' && *it <= 'Z')
            strInNew += *it-'A' + 'a';
    }
    int len = strInNew.length();
    for (int i = 0; i < len/2; i++) {
        if (strInNew[i] != strInNew[len-i-1]) {
            return false;
        }
        cout<<strInNew[i]<<" "<<strInNew[len-i-1]<<endl;
    }
    return true;
}


int main() {

    string input = "A man, a plan, a canal: Panama";
    cout<<checkPalindrome(input);

    return 0;
}
