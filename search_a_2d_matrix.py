class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0] > target:
            return False
        """
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
        """
        start = 0
        end = m - 1
        i = 0
        while start <= end:
            mid = start + (end - start) / 2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                start = mid + 1
            else:
                end = mid - 1
        i = end
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) / 2
            if target == matrix[i][mid]:
                return True
            elif target > matrix[i][mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False
