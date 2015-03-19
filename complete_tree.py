class Solution:
    def complete(self, root):
        if not root: return True
        num = 1 # num of nodes in the level
        queue = [root]
        while queue != []:
            tmp = []
            while queue != []:
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            num *= 2
            if len(tmp) < num:
                return False
            queue.append(tmp[:])

        return True
