#include <string>
#include <iostream>
#include <sstream>

using namespace std;

string* reverseWord(string str) {
    string* newStr = new string("");

    for (int i=0;i<str.size();i++){

    }
    return newStr;
}

int main(void) {

    string str = "abc cde  hahaha b";
    istringstream iss(str);
    string word;
    while(iss>>word);
    cout<<reverseWord(str);
    return 0;
}
