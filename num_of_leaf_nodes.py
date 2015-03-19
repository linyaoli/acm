class Solution:
    def getNum(self, root):
        if not root: return 0
        if not root.left and not root.right : return 1
        return self.getNum(root.left) + self.getNum(root.right)
