class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    _res = []
    def subsets(self, S):
      res = []
      self.gen(res, len(S), 0, S)
      self._res.append([])
      return self._res

    def gen(self, res, n, i, s):
      if i == n:
        return
      for j in xrange(i, n):
        res.append(s[j])
        self.gen(res, n, j + 1, s)
        self._res.append(res[:])
        res.pop()
