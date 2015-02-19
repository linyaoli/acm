# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        ans = []
        while True:
            if root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            else:
                if stack:
                    root = stack.pop()
                    root = root.right
                else:
                    break

        return ans
