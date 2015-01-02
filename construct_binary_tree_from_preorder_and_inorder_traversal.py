class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        n = len(inorder)
        return self.gen(inorder, 0, n - 1, preorder, 0, n - 1)

    def gen(self, inorder, instart, inend, preorder, prestart, preend):
        if instart > inend or prestart > preend:
            return None
        rootval = preorder[prestart]
        root = TreeNode(rootval)
        idx = 0
        for i in xrange(len(inorder)):
            if inorder[i] == rootval:
                idx = i
                break
        root.left = self.gen(inorder, instart, idx - 1, \
            preorder, prestart + 1, prestart + idx - instart)

        root.right = self.gen(inorder, idx + 1, inend,\
            preorder, prestart + idx - instart + 1, preend)

        return root
