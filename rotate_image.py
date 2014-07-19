class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix
        for i in xrange(n):
            for j in xrange(n-i):
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]
        for i in xrange(n/2):
            for j in xrange(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        return matrix
        
