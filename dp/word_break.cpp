/**
 * s = "catsanddog"
 * dict = ["cat", "cats", "and", "sand", "dog"]
 * ["cats and dog", "cat sand dog"]
 *
 */

#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
    public:
        bool wordBreakHelper(string s, vector<string> dict, int start) {
            if (start == s.length()) return true;
            vector<string>::iterator iter;
            for(iter=dict.begin(); iter<dict.end(); iter++) {
                int len = (*iter).length();
                int end = start + len;
                if (end > s.length())
                    continue;
                if (s.substr(start, start + len) == *iter) {
                    cout<<*iter<<" ";
                    if(wordBreakHelper(s, dict, start+len))
                        return true;
                }
            }
            return false;
        }

        bool wordBreak(string s, vector<string> dict) {
            return wordBreakHelper(s, dict, 0);
        }
};

int main(void) {

    string s("catsanddogmotherfucker");
    string dict_1[] = {"cat", "cats", "and", "sand", "dog", "mother", "fucker", "moth", "er"};
    vector<string> dict(dict_1, dict_1+9);

    Solution* a = new Solution();
    a->wordBreak(s, dict);
    return 0;
}
