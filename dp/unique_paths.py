class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        res = [[0]*m]*n
        for i in xrange(n):
            for j in xrange(m):
                if i > 0 and j > 0:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
                if i > 0 and j == 0:
                    res[i][j] = res[i - 1][j]
                if i == 0 and j > 0:
                    res[i][j] = res[i][j - 1]
                if i == 0 and j == 0:
                    res[i][j] = 1
        return res[i][j]
