# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        ret = [[root.val]]
        while q != []:
            tmp = []
            while q != []:
                t_n = q.pop(0)
                if t_n.left:
                    tmp.append(t_n.left)
                if t_n.right:
                    tmp.append(t_n.right)
            if tmp != []:
                tmp_ret = []
                for i in tmp:
                    tmp_ret.append(i.val)
                ret.append(tmp_ret)
                q += tmp
        return ret

            
