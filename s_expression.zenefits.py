"""
Input a list of parent-child pairs of binary tree : (A, B), (A, C), (B, G), (C, H), (E, F), (B, D), (C, E)
Output: (A(B(D)(G))(C(E(F))(H)))
Should be also available to identify errors.

Error Code      Type of error
E1                 More than 2 children
E2                 Duplicate Edges
E3                 Cycle present
E4                 Multiple roots
E5                 Any other error

so:
(A,B) (A,C) (B,D) (D,C)
-> E3

"""
class SExpression:
    def __init__(self):
        #transition table
        #self.table = [[0] * 26 for _ in xrange(26)]
        #transition map
        self.map = {}
    def get_exp(self, pairs):
        # initialize transition map
        for i in pairs:
            if i[0] in self.map:
                self.map[i[0]].append(i[1])
                self.map[i[0]].sort()
            else:
                self.map[i[0]] = [i[1]]
        err = self.err()
        if err: return err
        #find root
        root = None
        for i in self.map:
            root = i
            for j in self.map:
                if i in self.map[j]:
                    root = None
                    break
            if root:
                break

        #return s-expression
        ret = self.helper(root)
        return ret

    def helper(self, root):
        if root not in self.map:
            return root
        ret = root
        for i in self.map[root]:
            ret += '(' + self.helper(i) + ')'

        return ret


    def err(self):
        #check if any error exists

        #E2: Duplicate edges
        for i in self.map:
            if self.map[i] != sorted(list(set(self.map[i]))):
                return 'E2'
        #E1: more than two children.
        for i in self.map:
            if len(self.map[i]) > 2:
                return 'E1'

        #E3: Cycle present
        if self.findCycle():
            return 'E3'

        #E4: Multiple roots
        count = 0
        tmp = []
        for i in self.map:
            tmp += self.map[i]
        for i in self.map:
            if i not in tmp:
                count += 1
        if count > 1:
            return 'E4'
        #E5: any other error
        return None

    def findCycle(self):
        queue = [self.map.keys()[0]]
        visited = {self.map.keys()[0]:True}
        while queue != []:
            node = queue.pop(0)
            if node not in self.map: continue
            for i in self.map[node]:
                if i in visited:
                    return True
                queue.append(i)
                visited[i] = True

        return False



sol = SExpression()
print sol.get_exp([('A', 'B'), ('A', 'C'), ('B', 'G'), ('C', 'H'), ('E', 'F'), ('B', 'D'), ('C', 'E')])
sol.map = {}
print sol.get_exp([('B','D') ,('D','E'), ('A','B'), ('C','F'), ('E','G'), ('A','C')])
#(A(B(D(E(G))))(C(F)))
sol.map = {}
print sol.get_exp([('A','B'), ('A','C'), ('B','D'), ('D','C')])

sol.map = {}
print sol.get_exp([('A', 'C'), ('A', 'B'), ('A', 'D')])

sol.map = {}
print sol.get_exp([('A', 'C'), ('A', 'C'), ('A', 'D')])

sol.map = {}
print sol.get_exp([('A', 'C'), ('A', 'B'), ('D', 'E'), ('D', 'K')])
