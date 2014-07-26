class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        sol = []
        self.gen(n, k, 1, res, sol)
        return res
    def gen(self, n, k, lvl, res, sol):
        if len(sol) == k:
            res.append(sol)
            return
        for i in xrange(lvl, n+1):
            sol.append(i)
            self.gen(n, k, i+1, sol, res)
            sol.pop()
            
