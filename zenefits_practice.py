"""
Input: I want to buy a cup of water.
Output: I wnat to buy a cup of wtear.

Random the chars in a word(except two on the edge).

"""
import random as rd

class Solution (object):
    def sol1(self, s):
        i = 0
        j = 0
        s = list(s)
        while i <= len(s):
            if i == len(s) or s[i] == " ":
                if i > j:
                    n = i - j - 2
                    for k in xrange(j + 1, i - 1):
                        seed = int(rd.random() * n)
                        s[j + seed + 1], s[k] = s[k], s[j + seed + 1]
                j = i + 1
            i += 1

        return ''.join(s)


sol = Solution()
print sol.sol1("I want to buy a cup of water")
print sol.sol1("I am a tremendous shabi and never gonna fuck myself.")
