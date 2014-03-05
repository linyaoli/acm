#include <stdio.h>
#include <stdlib.h>

typedef struct BTree {
    struct BTree* left;
    struct BTree* right;
    int value;
}Node;

int countN(Node* node, int n) {
    if (node->left == NULL) {
        return 1;
    }
    if (node->right == NULL) {
        return 1;
    }

    return countN(node->left, n+1) + countN(node->right, n+1);

}
int main(void){


    Node* root = (Node*)malloc(sizeof(Node));
    root->value = 0;
    countN(root, 0);

    return 0;
}

