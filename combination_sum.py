class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = []
        self.gen(candidates, 0, len(candidates), res, [], target)
        return res

    def gen(self, s, i, n, res, sol, tar):
      if sum(sol) == tar:
        res.append(sorted(sol[:]))
      elif sum(sol) > tar:
        pass
      elif i == n:
        pass
      else:
        for j in xrange(i, n):
          sol.append(s[j])
          self.gen(s, j, n, res, sol, tar)
          sol.pop()
