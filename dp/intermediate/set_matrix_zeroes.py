class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix) #row
        n = len(matrix[0]) #col
        zero_row = 0
        zero_col = 0
        for i in xrange(n):
            if matrix[0][i] == 0:
                zero_row = 1
        for i in xrange(m):
            if matrix[i][0] == 0:
                zero_col = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zero_row == 1:
            for i in xrange(n):
                matrix[0][i] = 0
        if zero_col == 1:
            for i in xrange(m):
                matrix[i][0] = 0
