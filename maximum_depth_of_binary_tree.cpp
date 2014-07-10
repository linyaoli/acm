/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode *root) {
        if ( !root ) return 0;
        int _l = maxDepth( root->left );
        int _r = maxDepth( root->right );
        return 1 + (_l > _r? _l:_r);
    }
};
