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
        if not root:
            return []
        q = [root]
        ret = [[root.val]]
        while q != []:
            tmp = []
            while q != []:
                tmp_node = q.pop(0)
                if tmp_node.left:
                    tmp.append(tmp_node.left)
                if tmp_node.right:
                    tmp.append(tmp_node.right)
            if tmp != []:
                tmp_ret = []
                for i in tmp:
                    tmp_ret.append(i.val)
                ret.append(tmp_ret)
                q += tmp
        return ret[::-1]

        
