# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    # only have to use level order traversal.
    def rightSideView(self, root):
        if not root: return []
        q = [root]
        ret = [root.val]
        while q != []:
            tmp = []
            while q != []:
                node = q.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp != []:
                ret.append(tmp[-1].val)
                q += tmp

        return ret
