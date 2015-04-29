class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        p = [False] * n
        for i in xrange(1, n+1):
            for j in xrange(0, i):
                if s[j:i] in dict:
                    if j == 0:
                        p[i-1] = True
                    else:
                        # if s[:j] is consist of valid words.
                        # or s[:i] is a valid word.
                        p[i-1] = p[i-1] or p[j-1]
        return p[-1]


sol = Solution()
s = "sandand"
dict = ["san", "sand", "an", "and"]
#s = "a"
#dict = ["b"]
print sol.wordBreak(s, dict)
