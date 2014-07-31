# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        lis = []
        if root is not None:
            self.gen(root, sum, 0, res, lis)
        return res


    def gen(self, root, sum, n, res, lis):
        lis.append(root.val)
        n += root.val
        if n == sum and root.left is None and root.right is None:
            res.append(lis[:])
        else:
            if root.left is not None:
                self.gen(root.left, sum, n, res, lis)
            if root.right is not None:
                self.gen(root.right, sum, n, res, lis)
        lis.pop()
        n -= root.val
        return


        
