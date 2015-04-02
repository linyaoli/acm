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
        stack = []
        prev = None
        while stack != [] or root:
            cur = stack[-1]
            if not prev or prev.left == cur or prev.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
                elif cur.left == prev:
                    if cur.right:
                        stack.append(cur.right)
                    else:
                        print cur.data
                        stack.pop()
            prev = cur
    # use two stacks
    def postorderTraversal(self, root):
        if not root: return []
        stack1 = [root]
        stack2 = []
        prev = None
        ans = []
        while stack1 != []:
            prev = stack1.pop()
            stack2.append(prev)
            if prev.left:
                stack1.append(prev.left)
            if prev.right:
                stack1.append(prev.right)
        while stack2 != []:
            prev = stack2.pop()
            ans.append(prev.val)

        return ans
