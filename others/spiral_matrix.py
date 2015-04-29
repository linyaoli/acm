class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        self.helper(res, 0, 0, m, n, matrix)
        return res

    def helper(self, res, i, j, m, n, matrix):
        if i > m/2 and j > n/2:
            return

        if i < m - i - 1 and j < n - j - 1:
            for a in xrange(i, m-i-1):
                res.append(matrix[j][a])
            for a in xrange(j, n-j-1):
                res.append(matrix[a][m-i-1])

            for a in xrange(m-i-1, i, -1):
                res.append(matrix[n-j-1][a])

            for a in xrange(n-j-1, j, -1):
                res.append(matrix[a][i])

            self.helper(res, i+1, j+1, m, n, matrix)
        else:
            if i == m - i - 1:
                if j == n - j - 1:
                    print 1
                    res.append(matrix[i][j])
                else:
                    for a in xrange(j, n - j):
                        res.append(matrix[a][m-i-1])
            elif j == n - j - 1:
                for a in xrange(i, m - i):
                    res.append(matrix[n-j-1][a])

sol = Solution()

print sol.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
