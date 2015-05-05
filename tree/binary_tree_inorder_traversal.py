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
                root = root.left
            else:
                if stack:
                    root = stack.pop()
                    ans.append(root.val)
                    root = root.right
                else:
                    break

        return ans

    def inorderTraversal2(self, root):
        stack = []
        ans = []
        if not root: return ans
        while stack != [] or root:
            # always push left nodes at first.
            while root:
                stack.append(root)
                root = root.left
            # once done pushing, pop a node.
            # if it has right child, go right.
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
