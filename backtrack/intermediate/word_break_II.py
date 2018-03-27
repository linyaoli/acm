#!/usr/bin/python
class Solution:
    def wordBreak(self, s, dict):
        if dict == []:
            return []
        res = []
        # optimization, [i, n] is valid
        possible = [True for _ in xrange(len(s)+1)]
        self.helper(0, s, dict, res, [], possible)
        return res

    def helper(self, i, s, dict, res, sol, pos):
        if i == len(s):
            res.append(" ".join(sol))
        else:
            for j in xrange(i, len(s)):
                if s[i:j+1] in dict and pos[j+1]:
                    sol.append(s[i:j+1])
                    sz = len(res)
                    self.helper(j+1, s, dict, res, sol, pos)
                    if sz == len(res):
                        pos[j+1] = False
                    sol.pop()


sol = Solution()

s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
s = "aaaaaaa"
dict = ["aaaa", "aaa"]
#["cats and dog", "cat sand dog"]
print sol.wordBreak(s, dict)
