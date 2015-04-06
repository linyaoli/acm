"""
http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
LCS for input Sequences AGGTAB and GXTXAYB is GTAB of length 4.

"""
class Solution:
    def longestCommonSubsequence(self, s1, s2):
        dp = [[0 for _ in xrange(len(s1) + 1)] for _ in xrange(len(s2) + 1) ]
        for i in xrange(len(s1)+1):
            for j in xrange(len(s2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(s1)][len(s2)]

sol = Solution()
print sol.longestCommonSubsequence("ABCDGH", "AEDFHR")
