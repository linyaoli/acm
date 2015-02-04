"""
dp[i][j] =  | dp[i-1][j-1] + 1 if word1[i] == word2[j]
            | max(dp[i][j-1], dp[i-1][j])

dp[0][j] = 0
dp[i][0] = 0

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

consider somestr1c -> somestr2d:
if somestr1 -> somestr2 is dp[i-1][j-1]
somestr1c -> somestr2 is dp[i][j-1]
somestr1 -> somestr2d is dp[i-1][j]

thus,

if c == d:
    dp[i][j] = dp[i-1][j-1]
if c != d:
    1> replace c with d:  dp[i][j] = dp[i-1][j-1] + 1
    2> insert d after c:  dp[i][j] = dp[i][j-1] + 1
    3> delete c: dp[i][j] = d[i-1][j] + 1

    find min(1,2,3)

"""
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        matchUp = [0] * 20000
        matchDown = [0] * 20000
        len_a = len(word1)
        len_b = len(word2)

        for i in xrange(max(len_a, len_b) + 1):
            matchUp[i] = 0
            matchDown[i] = i
        for i in xrange(1, len_a + 1):
            matchUp[0] = i
            for j in xrange(1, len_b + 1):
                if word1[i - 1] == word2[j - 1]:
                    matchUp[j] = matchDown[j - 1]
                else:
                    matchUp[j] = min(matchDown[j], matchDown[j - 1])
                    matchUp[j] = min(matchUp[j], matchUp[j - 1]) + 1
            matchUp, matchDown = matchDown, matchUp

        return matchDown[len_b]

sol = Solution()
print sol.minDistance("abcd", "aacbd")
