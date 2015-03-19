class Solution:
    def getNum(self, root, n):
        return self.helper(root, 1, n)

    def helper(self, root, i, n):
        if not root: return 0
        if i == n:
            return 1
        return self.helper(root.left, i+1, n) + self.helper(root.right, i+1, n)
