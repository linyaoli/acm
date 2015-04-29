#include <iostream>

typedef struct Tree {
    struct Tree* left;
    struct Tree* right;
    int val;
}root;

int findNummRootLeaf(root* node) {

    if (node == NULL)
        return 0;
    else
        return 1 + findNummRootLeaf(node->left);

}
// not finished, later.
// FIXME
int main() {

    return 0;
}
