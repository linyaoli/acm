# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        stk = [root]
        result = []
        while len(stk) != 0:
            tmpList = []
            tmpValList = []
            while len(stk) != 0:
                root = stk.pop(0)
                if root is not None:
                    tmpList.append(root)
                    tmpValList.append(root.val)

            result.append(tmpValList)

            for i in xrange(len(tmpList)):
                root = tmpList[i]
                if root.left is not None:
                    stk.append(root.left)
                if root.right is not None:
                    stk.append(root.right)

        res_ = []
        for i in xrange(len(result)-1, -1, -1):
            if result[i] != []:
                res_.append(result[i])

        return res_





        
