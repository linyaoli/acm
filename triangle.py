#Leetcode question : triangle.

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
totallv = 4

dp = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
result = 0

# bot-up iteratively
for i in range(totallv - 1, -1, -1):
    for j in range(0, i + 1, 1):
        if dp[i][j] == 0:
            if i == totallv - 1:
                dp[i][j] = triangle[i][j]
            else:
                dp[i][j] = dp[i + 1][j] + triangle[i][j]
        tmp1 = triangle[i][j] + dp[i + 1][j + 1]
        tmp2 = triangle[i][j] + dp[i + 1][j]
        if tmp1 < dp[i][j]:
            dp[i][j] = tmp1
        if tmp2 < dp[i][j]:
            dp[i][j] = tmp2

print "By dynamical programming, we have a solution of O(n)"
print dp
