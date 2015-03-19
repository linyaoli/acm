class Solution:
    def convert(self, root):
        if not root.left and not root.right: return root

        if root.left:
            l_child = self.convert(root.left)
            while l_child.right:
                l_child = l_child.right
            l_child.right = root
            root.left = l_child
        if root.right:
            r_child = self.convert(root.right)
            while r_child.left:
                r_child = r_child.left
            r_child.left = root
            root.right = r_child

        return root
