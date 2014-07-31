# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.gen(1,n)

    def gen(self, begin, end):
        solution = []
        if begin > end:
            solution.append(None)
            return solution
        for root in range(begin,end+1):
            leftNodes = self.gen(begin, root-1)
            rightNodes = self.gen(root+1, end)

            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    node = TreeNode(root)
                    node.left = leftNode
                    node.right = rightNode
                    solution.append(node)
        return solution
