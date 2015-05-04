"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving

the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        s2t = {}# src to tar
        t2s = {}# tar to src
        for i in xrange(len(s)):
            if s[i] not in s2t:
                if t[i] not in t2s:
                    s2t[s[i]] = t[i]
                    t2s[t[i]] = s[i]
                else:
                    return False
            else:
                if s2t[s[i]] != t[i]:
                    return False

        return True


sol = Solution()
print sol.isIsomorphic("title", "paper")
