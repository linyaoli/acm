# Definition for a  binary tree node
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        self.validate(root, -10000, 10000)

        
    def validate(self, root, max_int, min_int)
        if not root.left and not root.right:
            return max(root.val, max_int), min(root.val, min_int)
        max_cur = min_cur = 0
        if root.left:
            max_cur, min_cur = self.validate(root.left, max_int, min_int)
        if root.right:
            max_cur, min_cur = self.validate(root.right, max_int, min_int)

        if max_cur > root.val or min_cur < r
