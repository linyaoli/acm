#!/usr/bin/python
class Solution:
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return False
        s = '#' + s
        _len = len(s)
        p = [False] * _len
        p[0] = True
        for i in range(1, _len, 1):
            for j in range(0, i, 1):
                if s[j + 1:i + 1] in dict:
                    p[i] = p[j]
                else:
                    p[i] = False
                if p[i]:
                    break
        print s
        print dict
        print p
        return p[_len - 1]

sol = Solution()
#s = "abcdefg"
#dict = ["a", "bc", "bcd", "ef", "efg"]
s = "a"
dict = ["b"]
print sol.wordBreak(s, dict)
