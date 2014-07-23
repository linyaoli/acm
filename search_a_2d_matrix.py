class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        m = len(matrix) - 1
        n = 0
        while m >= 0 and n >= 0:
            if matrix[m][n] == target:
                return True
            if matrix[m][n] < target:
                n += 1
            if n > len(matrix[0]) - 1:
                return False
            if matrix[m][n] > target:
                m -= 1
            if m < 0:
                return False
          
