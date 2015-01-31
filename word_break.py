#!/usr/bin/python
class Solution:
    def wordBreak(self, s, dict):
        n = len(dict)
        if n == 0:
            return False
        p = [False] * len(s)
        n = len(s)
        for i in xrange(1, n + 1):
            for j in xrange(0, i):
                if s[j:i] in dict:
                    if j == 0:
                        p[i-1] = True
                    else:
                        p[i-1] = p[j-1] or p[i-1]
        return p[-1]


sol = Solution()
s = "sandand"
dict = ["san", "sand", "an", "and"]
#s = "a"
#dict = ["b"]
print sol.wordBreak(s, dict)
