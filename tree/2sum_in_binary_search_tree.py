"""
find 2 nodes in a binary search tree which make a + b = k.
"""
class Solution :
    def twosum(self, root, k):
        # naive solution
        # inorder traversal -> array -> 2sum problem. O(n) time O(n) space.
        # optimization:
        # Cannot improve time, only space to O(logn) by using stack.
        stack_left = []
        stack_right = []
        node1 = root
        node2 = root
        # left most -> smallest
        while node1:
            stack_left.append(node1)
            node1 = node1.left
        # right most -> largest
        while node2:
            stack_right.append(node2)
            node2 = node2.right
        # 2 sum problem
        while len(stack_left) > 0 and len(stack_right) > 0:
            if stack_left[-1].val + stack_right[-1].val < k:
                node = stack_left.pop()
                if node.right:
                    stack_left.append(node.right)
                    node = node.right.left
                    while node:
                        stack_left.append(node)
                        node = node.left
            elif stack_left[-1].val + stack.right[-1].val > k:
                node = stack_right.pop()
                if node.left:
                    stack_right.append(node.left)
                    node = node.left.right
                    while node:
                        stack_right.append(node)
                        node = node.right
            else:
                return node_right[-1], node_left[-1]

        return None
