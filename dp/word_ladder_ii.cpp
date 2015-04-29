#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> result;

int operator-(const string& minuend, const string& subtractor);

bool isPresent(vector<string> vec,string target) {
    if (std::find(vec.begin(), vec.end(), target) != vec.end())
        return true;
    else
        return false;
}

int ladder(string start, string end, string dict[], int dictlen, int level) {
    if (level >= 4) return 0;
    for (int i = 0;i < dictlen; i++) {
        if (start - end != -1) {
            result.push_back(end);
            for (vector<string>::iterator it=result.begin(); it != result.end(); ++it) {
                cout<<*it<<" ";
            }
            cout<<endl;
            result.pop_back();
        }

        int re = start - dict[i];
        if (re == -1) continue;
        if  (isPresent(result, dict[i]) == true)
            continue;
        else
            result.push_back(dict[i]);
        ladder(dict[i], end, dict, dictlen, level+1);
        result.pop_back();
    }
    //int hash_table[26] = {0};
    //for (int i = 0; i < dictlen; i++) {
        //for (int j = 0; j < wordlen; j++) {
            //hash_table[dict[i].at(j) - 'a'] = 1;
        //}
        //int count = 0;
        //for (int j = 0; j < wordlen; j++) {
            //if (hash_table[start.at(j) - 'a'] == 1)
                //count++;
        //}
        //if (count == wordlen-1) {//meaning only one char is different.
            //for (int j = 0; j < wordlen; j++){

            //}
        //}
    //}
    //return 0;


    return 0;
}
//find the different charactor.
int operator-(const string& minuend, const string& subtractor) {
    if (minuend == "" || subtractor == "") return -1;
    int a_len = minuend.length();
    int b_len = subtractor.length();
    if (a_len != b_len) return -1;
    //////////////
    string returner = "";
    int counter = 0;
    int first_diff = 0;
    int do_once = 0;
    for (int i = 0; i < a_len; i++) {
        if (minuend[i] != subtractor[i]) {
            counter ++;
            if (do_once == 0) {
                first_diff = i;
                do_once = 1;
            }
        }
    }

    if (counter == 1)
        return first_diff;
    else
        return -1;
}

int main() {

    string start = "hit";
    string end = "cog";
    string dict[5] = {"hot", "dot", "dog", "lot", "log"};

    result.push_back(start);
    ladder(start, end, dict, 5, 0);

    return 0;
}
