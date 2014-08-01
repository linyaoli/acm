class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
      res = []
      sol = []
      self.gen(0 ,len(digits), res, sol, digits)
      return sol

    def gen(self, i, n, res, sol, digits):
      if i == n and len(res) == len(digits):
        tmp = ""
        for item in res:
          tmp += item
        sol.append(tmp)
      else:
        for j in xrange(i, n):
          for item in self.letters(digits[j]):
            res.append(item)
            self.gen(j + 1, n, res, sol, digits)
            res.pop()

    def letters(self, num):
      return {
        '1': "",
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
        '0': " "
      }[num]
