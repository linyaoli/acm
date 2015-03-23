#include <vector>
#include <iostream>
using namespace std;
void sort_array(vector<int>& s){
    int n = (int)s.size();
    if(n == 0) return;

    bool flag = true;
    int current = s[0];
    for (int i = 0; i < n-1; i++) {
        if ((flag && current > s[i+1]) || (!flag && current < s[i+1])) {
            s[i] = s[i+1];
        } else {
            s[i] = current;
            current = s[i+1];
        }
        flag = !flag;
    }
    s[n-1] = current;
}


int main(){
  int vv[5] = {1,4,5,2,3};
  std::vector<int> s(&vv[0], &vv[0]+5);
  sort_array(s);
  for (int i = 0; i < s.size(); i++){
    cout << s[i] << " ";
  }
  return 0;
}
