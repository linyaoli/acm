class Solution:
    def lca(self, root, node1, node2):
        if not root or not node1 or node2:
            return None
        if root == node1 or root == node2:
            return root
        left = self.lca(root.left, node1, node2)
        right = self.lca(root.right, node1, node2):
        if left and right:
            return root
        else:
            return left or right
