#include <iostream>
using namespace std;

int board[4][4] ={{0,1,1,1},{1,0,0,1},{1,1,0,1},{1,0,1,1}};
int m[4][4] = {0};
// ugly written, but really works.
bool search(int size, int pos_x, int pos_y) {
    //m[i][j]= 1while point borad[i][j] is visited.
    if (m[pos_x][pos_y] == 1)
        return true;
    for(int i=0;i<4;i++) {
        for(int j=0;j<4;j++)
            cout<<board[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
    if (pos_x == 0 || pos_y == 0) {
        if (board[pos_x][pos_y] == 0)
            return false;
        else if (board[pos_x][pos_y] == 1)
            return true;
    }
    else if (board[pos_x][pos_y] == 1)
        return true;
    else {
        m[pos_x][pos_y] = 1;
        return search(size, pos_x-1, pos_y) &&
        search(size, pos_x, pos_y-1) &&
        search(size, pos_x, pos_y+1) &&
        search(size, pos_x+1, pos_y) ;
    }
    return true;
}
int main() {
    int i, j;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 4; j++) {
            if (board[i][j] == 0) {
                if (search(4, i, j) == true) {
                    board[i][j] = 1;
                }
                for (int aa=0;aa<4;aa++)
                    for (int bb=0;bb<4;bb++)
                        m[aa][bb] = 0;
            }
        }

    return 0;
}
