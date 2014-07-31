class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        n = len(S)
        res = []
        sub = []
        res.append([])
        self.gen(0, n, res, sub, S)
        return res


    def gen(self, i, n, res, sub, S):
      if i == n:
        return
      else:
        for j in xrange(i, n):
          sub.append(S[j])
          self.gen(j + 1, n, res, sub, S)
          if sub[:] not in res:
            res.append(sub[:])
          sub.pop()
