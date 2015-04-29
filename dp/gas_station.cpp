#include <iostream>

using namespace std;

int main(void) {

    int gas[10] = {1,3,3,5,1,7,2,3,4,5};
    int cost[10] = {1,1,3,3,2,4,2,3,1,2};
    int tank = 1; // assume start from station 0
    for (int i = 1;i < 10; i++) {
        if (tank >= cost[i]) {
            tank = tank - cost[i];
            tank += gas[i];
        }
        else
            break;
        cout<<"tank:"<<tank<<" next station cost:"<<cost[i]<<endl;

    }


    return 0;
}
