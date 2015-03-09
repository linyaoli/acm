#include <iostream>
#include <vector>
using namespace std;

int  main(){

  int* a = new int[10];
  a[0] = 1;
  cout<<a[0]<<endl;

  delete a;


}
