class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = []
        self.target = target
        self.gen(candidates, 0, len(candidates), res, [])
        return res

    def gen(self, s, i, n, res, sol):
        if sum(sol) == self.target:
            res.append(sorted(sol[:]))
        elif sum(sol) > self.target or i == n:
            return
        else:
            for j in xrange(i, n):
                sol.append(s[j])
                self.gen(s, j, n, res, sol)
                sol.pop()


sol = Solution()
print sol.combinationSum([1,2,3,4,5,6,7], 5)
