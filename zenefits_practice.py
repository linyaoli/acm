"""
Input: I want to buy a cup of water.
Output: I wnat to buy a cup of wtear.

Random the chars in a word(except two on the edge).

"""
import random as rd

class Solution (object):
    def sol1(self, s):
        s = s.split(' ')
        for i in xrange(len(s)):
            s[i] = self.helper(s[i])

        return ' '.join(s)

    def helper(self, s):
        s = list(s)
        for i in xrange(1, len(s) - 1):
            seed = int(rd.random() * (len(s) - 2)) + 1
            s[i], s[seed] = s[seed], s[i]
        return ''.join(s)



sol = Solution()
print sol.sol1("I want to buy a cup of water")
print sol.sol1("I am a tremendous shabi and never gonna fuck myself.")
print sol.sol1("abc abcdefg a ab abcd")
