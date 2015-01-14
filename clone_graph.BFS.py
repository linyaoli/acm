# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        copyNode = UndirectedGraphNode(node.label)
        nodeMap = {}
        nodeMap[node] = copyNode
        visited = [node]
        while visited:
            cur = visited.pop()
            for _n in cur.neighbors:
                if _n not in nodeMap:
                    nd = UndirectedGraphNode(_n.label)
                    nodeMap[cur].neighbors.append(nd)
                    nodeMap[_n] = nd
                    visited.append(_n)
                else:
                    nodeMap[cur].neighbors.append(nodeMap[_n])

        return copyNode
