"""
There are n coins in a line. (Assume n is even). Two players take turns to take
a coin from one of the ends of the line until there are no more coins left.
The player with the larger amount of money wins.

1. Would you rather go first or second? Does it matter?
2. Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.

"""
# If go first , we have the advantages of:
# 1. pick the larger one at first.
# 2. if the num is odd, we can pick one more coin.

# dp[i][j] gives the solution of coin i to coin j, which is the maximum amount.
# sum[i][j] is the total amount of coin i to coin j.
# Therefore, for every sub problem:
# if you pick the first one, the problem becomes (i+1, j), thus your opponent can get the solution from dp[i+1][j].
# and you can gain the money sum[i+1][j] - dp[i+1][j].

# dp[i][j] = max(sum[i][j]-dp[i+1][j], sum[i][j]-dp[i][j-1])
#
#          = sum[i][j]-min(dp[i+1][j],dp[i][j-1])


class Solution:
    def coins(self, arr):
        n = len(arr)
        sum = [[0 for _ in xrange(n)] for _ in xrange(n)]
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        # initialize the sum array
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if i == j:
                    sum[i][j] = arr[j]
                else:
                    sum[i][j] = arr[j] + sum[i][j-1]
        # 
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if i == j:
                    dp[i][j] = arr[i]
                else:
                    dp[i][j] = sum[i][j] - min(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]
