class Solution:
    def get(self, root):
        self.max1 = -999
        self.max2 = -999

    def helper(self, root):
        if not root: return
        if root.val > self.max1:
            max2 = max1
            max1 = root.val
        elif root.val > self.max2:
            max2 = root.val

        if root.right:
            self.helper(root.right)
        elif root.left:
            self.helper(root.left)

    # this algorithm also works for 2nd smalleset in bst.        
