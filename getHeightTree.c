int max = 0;
int getHeight(Node* root, int n) {

    if(n > max)
        max = n;
    if(root->left != NULL)
        getHeight(root->left, n+1);
    if(root->right != NULL)
        getHeight(root->right, n+1);
}
int main() {

    getHeight(root, 1);
    return 0;
}
