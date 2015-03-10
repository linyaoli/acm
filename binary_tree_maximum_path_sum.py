# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.
@@@@@

There are four conditions that we need to consider in each node:

           node
          /    \
         /      \
left subtree    right subtree

1> left subtree + node.val
2> right subtree + node.val
3> left subtree + right subtree + node.val
4> node.val

bot-up solution

"""

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxsum = -2**31
        self.helper(root)
        return self.maxsum

    def helper(self, root):
        if not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.maxsum = max(self.maxsum, left + right + root.val)
        ret = root.val + max(left, right)
        if ret > 0:
            return ret
        else:
            #TODO: do not include this subtree in higher calculation cuz it's negative.
            return 0
