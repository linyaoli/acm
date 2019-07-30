# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.helper(1, n)

    def helper(self, start, end):
        solution = []
        if start > end:
            solution.append(None)
            return solution
        for root in xrange(start, end + 1):
            leftNodes = self.helper(start, root - 1)
            rightNodes = self.helper(root + 1, end)
            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    node = TreeNode(root)
                    node.left = leftNode
                    node.right = rightNode
                    solution.append(node)
        return solution
