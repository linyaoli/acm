class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        sol = []
        self.gen(n, k, 0, res, sol)
        return res
    def gen(self, n, k, start, res, sol):
        if len(sol) == k:
            res.append(sol[:])
        else:
          for i in xrange(start, n):
              sol.append(i+1)
              self.gen(n, k, i+1, res, sol)
              sol.pop()

sol = Solution()
print sol.combine(4, 2)
