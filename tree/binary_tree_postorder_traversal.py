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

    # use one stack
    def postorderIterative2(self, root):
        if not root : return []
        stack = [root]
        ans = []
        while stack != []:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                ans.append(root.val)
                root = None
        return ans

    # use two stacks
    def postorderTraversal(self, root):
        if not root: return []
        stack1 = [root]
        stack2 = []
        ans = []
        while stack1 != []:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2 != []:
            node = stack2.pop()
            ans.append(node.val)

        return ans
