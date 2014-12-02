# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0 \
            or len(preorder) != len(inorder):
            return None

        root = TreeNode(preorder[0])
        mid = 0
        for i in xrange(len(inorder)):
            if inorder[i] == root.val:
                mid = i

        left = TreeNode(preorder[1])
        right = TreeNode(preorder[mid + 1])
        root.left = left
        root.right = right

        self.gen(root.left, preorder[1:mid + 1], inorder[:mid])
        self.gen(root.right, preorder[mid + 1:], inorder[mid:])

    def gen(self, root, preorder, inorder):
        mid = 0
        for i in xrange(len(inorder)):
            if inorder[i] == root.val:
                mid = i
        left = TreeNode(preorder[1])
        right = TreeNode(preorder[mid + 1])
        root.left = left
        root.right = right
        
        self.gen(root.left, preorder[1:mid + 1], inorder[:mid])
        self.gen(root.right, preorder[mid + 1:], inorder[mid:])
