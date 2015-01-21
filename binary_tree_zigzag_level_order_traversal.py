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
        if not root:
            return []
        queue = [root]
        arr = []
        res = [[root.val]]
        tmp = []
        counter = 0
        while queue != []:
            while queue != []:
                node = queue.pop(0)
                if counter % 2 == 0:
                    if node.left:
                        arr.append(node.left)
                    if node.right:
                        arr.append(node.right)
                else:
                    if node.right:
                        arr.append(node.right)
                    if node.left:
                        arr.append(node.left)
            for node in arr[::-1]:
                queue.append(node)
                tmp.append(node.val)
            if tmp != []:
                res.append(tmp)
            arr = []
            tmp = []
            counter += 1

        return res

            
