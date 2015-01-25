# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        _stack = []
        _val = []
        while True:
            if root != None:
                _stack.append(root)
                root = root.left
            else:
                if _stack != []:
                    root = _stack.pop()
                    _val.append(root.val)
                    root = root.right
                else:
                    break


        return _val








            
