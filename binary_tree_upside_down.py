"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left
node that shares the same parent node) or empty, flip it upside down and turn it into a tree
where the original right nodes turned into left leaf nodes. Return the new root.

          1             4
         / \           / \
        2   3    =>   5   2
       / \               / \
      4   5             3   1
"""

class Solution:

    def upsideDown_topdown(self, root):
        p = root
        parent = None
        parentRight = None
        while p:
            left = p.left
            p.left = parentRight
            parentRight = p.right
            p.right = parent
            parent = p
            p = left
        return parent

    def upsideDown_botup(self, root):
        return self.helper(root, None)

    def helper(self, root, parent):
        if not root: return parent
        p = self.helper(root.left, root)
        if parent:
            root.left = parent.right
        else:
            root.left = None
        root.right = parent
        return p
