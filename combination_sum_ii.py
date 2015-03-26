class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        res = []
        self.helper(candidates, len(candidates), 0, target, [], res)
        return res

    def helper(self, s, n, i, tar, sol, res):
        if tar < 0:
            return
        elif i <= n and tar == 0:
            sol = sorted(sol)
            if sol not in res:
                res.append(sol)
        else:
            for m in xrange(i, n):
                sol.append(s[m])
                self.helper(s, n, m+1, tar-s[m], sol, res)
                sol.pop()

# can use hash to avoid calculate duplicate nums.

sol = Solution()
print sol.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,
9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,
32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27)
