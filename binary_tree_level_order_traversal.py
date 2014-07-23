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
        if root is None:
            return []
        res = []
        queue = [root]
        tmp_res = []
        visited = 0
        cur_lvl = 1
        next_lvl = 0
        while queue != []:
            node = queue.pop(0)
            tmp_res.append(node.val)
            visited += 1
            if node.left is not None:
                queue.append(node.left)
                next_lvl += 1
            if node.right is not None:
                queue.append(node.right)
                next_lvl += 1
            if visited == cur_lvl:
                visited = 0
                cur_lvl = next_lvl
                next_lvl = 0
                res.append(tmp_res)
                tmp_res = []
        return res




            
