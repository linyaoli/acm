void posttraversal(Tree* root) {

    if (!root)
        printf("#");
    posttraversal(root->left);
    posttraversal(root->right);
    printf("%d", root->val);
}
