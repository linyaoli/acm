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
