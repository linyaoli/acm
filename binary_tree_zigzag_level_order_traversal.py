# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        reversed = 0
        q = []
        res = []
        q.append(root)
        while len(q) != 0:
            cur = []
            _res = []
            while len(q) != 0:
                node = q.pop(0)
                if node.left is not None:
                    cur.append(node.left)
                if node.right is not None:
                    cur.append(node.right)
                _res.append(node)
            if reversed == 0:
                reversed = 1
                tmp = []
                for item in _res:
                    tmp.append(item.val)
                res.append(tmp[:])
            else:
                reversed = 0
                tmp = []
                aaa = _res
                aaa.reverse()
                for item in aaa:
                    tmp.append(item.val)
                res.append(tmp[:])
            q += cur

        return res
                
