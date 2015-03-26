# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # O(n**2)
    def cloneGraph(self, node):
        if not node:
            return None
        copyNode = UndirectedGraphNode(node.label)
        nodeMap = {}
        nodeMap[node] = copyNode
        queue = [node]
        while queue:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n not in nodeMap:
                    cp = UndirectedGraphNode(n.label)
                    nodeMap[n] = cp
                    #nodeMap[cur] -> copied node
                    nodeMap[cur].neighbors.append(cp)
                    queue.append(n)
                else:
                    nodeMap[cur].neighbors.append(nodeMap[n])

        return copyNode
"""
    def cloneGraph2(self, node):
        if not node: return None
        nodemap = {}
        visited = [node]
        cp = UndirectedGraphNode(node.label)
        cloned = [cp]
        nodemap[node] = cp
        while visited:
            cur = visited.pop()
            for n in cur.neighbors:
                if n not in nodemap:
                    node = UndirectedGraphNode(n.label)
                    cloned.append(node)
                    nodemap[cur] = node
                    visited.append(n)
        for node in cloned:
            for n in node.neighbors:
                n = nodemap[n]

        return cp
"""
