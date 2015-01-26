class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S = sorted(S)
        self.gen(0, len(S), S, [], res)
        return res

    def gen(self, i, n, S, sub, res):
        if i == n:
            return

        for j in xrange(i, n):
            sub.append(S[j])
            self.gen(j + 1, n, S, sub, res)
            if sub[:] not in res:
                res.append(sub[:])
            sub.pop()


sol = Solution()
print sol.subsetsWithDup([0])
