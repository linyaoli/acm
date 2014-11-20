class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        res = [], sol = []        
        self.gen(candidates, 0, len(candidates), res, sol, target)
        return res

    def gen(self, can, i, n, res, sol, tar):
      if sum(sol) == tar:
        res.append(sorted(sol[:]))
        return
      elif sum(sol) > tar:
        return
      elif i == n:
        return
      else:
        for j in xrange(i, n):
          sol.append(can[j])
          self.gen(can, j, n, res, sol, tar)
          sol.pop()
