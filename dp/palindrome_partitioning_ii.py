class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        n = len(s)
        # min_cur[i] : the minimal cut of s[i:n]
        min_cut = [n-i for i in xrange(n+1)]
        # p[i][j] = True -> [i, j] is palindrome
        # p[i][j] = (str[i] == str[j] && p[i+1][j-1])
        p = [[False] * n for _ in xrange(n)]

        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if s[i] == s[j] and (j - i < 2 or p[i+1][j-1]):
                    p[i][j] = True
                    min_cut[i] = min(min_cut[i], min_cut[j+1]+1)

        return min_cut[0] - 1
