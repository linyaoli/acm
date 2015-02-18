class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        n = len(inorder)
        return self.gen(inorder, 0, n - 1, postorder, 0, n - 1)

    def gen(self, inorder, instart, inend, postorder, poststart, postend):
        if instart > inend or poststart > postend:
            return None
        rootval = postorder[postend]
        root = TreeNode(rootval)
        idx = 0
        for i in xrange(len(inorder)):
            if inorder[i] == rootval:
                idx = i
                break

        root.left = self.gen(inorder, instart, idx - 1, \
            postorder, poststart, poststart + idx - (instart + 1))

        root.right = self.gen(inorder, idx + 1, inend, postorder, poststart + idx - instart, \
            postend - 1)

        return root

sol = Solution()
sol.buildTree([4,2,5,1,6,3,7], [1,2,4,5,3,6,7])
