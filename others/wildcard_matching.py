"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

isMatch("aa","a")  false
isMatch("aa","aa")  true
isMatch("aaa","aa")  false
isMatch("aa", "*")  true
isMatch("aa", "a*")  true
isMatch("ab", "?*")  true
isMatch("aab", "c*a*b")  false

"""
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        star = -1
        match = 0
        i, j = 0, 0
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                # TODO: deal with '*'
                # save the current i and j.
                # set j to the next character.
                match = i
                star = j
                j += 1
            elif star != -1:
                # TODO: compare until s[i] == p[j]
                # if the current match results into a wrong result.
                # we start from j = star + 1 again, find the next match.
                j = star + 1
                match += 1
                i = match
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)


sol = Solution()
print sol.isMatch("aaa", "*")
