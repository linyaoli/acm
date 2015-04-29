class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        self.k = k
        self.gen(n, 0, res, [])
        return res

    def gen(self, n, start, res, sol):
        if len(sol) == self.k:
            res.append(sol[:])
        else:
          for i in xrange(start, n):
              sol.append(i+1) # if append(i) => [0,1] not [1,2]
              self.gen(n, i+1, res, sol)
              sol.pop()

sol = Solution()
print sol.combine(4, 2)
