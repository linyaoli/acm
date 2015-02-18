class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        best = [triangle[0][0]]
        for i in xrange(1, n):
            m = len(triangle[i])
            _best = best
            best = []
            for j in xrange(0, m):
                if j == 0:
                    best.append(_best[0] + triangle[i][j])
                elif j == m - 1:
                    best.append(_best[-1] + triangle[i][j])
                else:
                    best.append(min(_best[j], _best[j - 1]) + triangle[i][j])

        return min(best)
