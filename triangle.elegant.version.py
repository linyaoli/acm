"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]


"""
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        best = [[0] * n for _ in range(n)]
        best[0][0] = triangle[0][0]

        for i in xrange(1, n):
            m = len(triangle[i])
            for j in xrange(0, m):
                if j == 0:
                    best[i][j] = best[i - 1][j] + triangle[i][j]
                elif j == m - 1:
                    best[i][j] = best[i - 1][j - 1] + triangle[i][j]
                else:
                    best[i][j] = min(best[i - 1][j], best[i - 1][j - 1]) + triangle[i][j]

        return min(best[-1])
