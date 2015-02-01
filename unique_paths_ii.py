class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        _res = obstacleGrid
        n = len(_res)
        m = len(_res[0])
        if _res[-1][-1] == 1:
            return 0
        res = [[0] * m] * n
        for i in xrange(n):
            for j in xrange(m):
                if _res[i][j] == 1:
                    res[i][j] = 0
                    continue
                if i > 0 and j > 0:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
                elif i > 0 and j == 0:
                    res[i][j] = res[i - 1][j]
                elif i == 0 and j > 0:
                    res[i][j] = res[i][j - 1]
                elif i == 0 and j == 0:
                    res[i][j] = 1
        return res[i][j]
