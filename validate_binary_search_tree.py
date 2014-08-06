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
        trav = []
        self.gen(trav, root)
        for i in xrange(len(trav) - 1):
            if trav[i] >= trav[i + 1]:
                return False
        return True

    def gen(self, trav, root):
        if root is None:
            return
        self.gen(trav, root.left)
        trav.append(root.val)
        self.gen(trav, root.right)


            
