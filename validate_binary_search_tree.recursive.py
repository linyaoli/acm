# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.validate(root, 10000000000, -10000000000)


    def validate(self, root, max_int, min_int):
        if not root:
            return True

        if root.val > min_int and root.val < max_int:
            return self.validate(root.left, root.val, min_int) and self.validate(root.right, max_int, root.val)
        else:
            return False
