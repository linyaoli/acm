class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S = sorted(S)
        res = []
        sol = [[]]
        self.gen(res, len(S), 0, S, sol)

        return sol

    def gen(self, res, n, i, s, sol):
        if i == n:
            return
        for j in xrange(i, n):
            res.append(s[j])
            # every element can be in or not in.
            self.gen(res, n, j + 1, s, sol)
            sol.append(res[:])
            res.pop()


sol = Solution()
print sol.subsets(['x','y','z'])
