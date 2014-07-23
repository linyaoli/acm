# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []
        res = []
        self._postorderTraversal(root, res)
        return res

    def _postorderTraversal(self, root, res):
        if root is None:
            return
        self._postorderTraversal(root.left, res)
        self._postorderTraversal(root.right, res)
        res.append(root.val)
        
