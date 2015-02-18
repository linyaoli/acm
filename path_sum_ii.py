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
        ret = []
        self.helper(root, ret, [], total=sum)
        return ret

    def helper(self, root, ret, path, total):
        if not root:
            return 0
        #is leaf node
        path.append(root.val)
        if not root.left and not root.right:
            if total == sum(path):
                ret.append(path[:])
        else:
            if root.left:
                self.helper(root.left, ret, path, total)
                path.pop()
            if root.right:
                self.helper(root.right, ret, path, total)
                path.pop()
