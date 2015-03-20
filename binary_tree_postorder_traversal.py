# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root: return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root: return
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

    def postorderIterative(self, root):
        if not root : return
        s = [root]
        prev = None
        while s != []:
            curr = s[-1]
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    s.append(curr.left)
                elif curr.right:
                    s.append(curr.right)
                elif curr.left == prev:
                    if curr.right:
                        s.append(curr.right)
                    else:
                        print curr.data
                        s.pop()
            prev = curr

            
