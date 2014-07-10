class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A == []:
            return 0
        _len = len(A)
        start = 0
        end = _len - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            if mid > start and A[mid] > target and A[mid - 1] < target:
                return mid
            if A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

            
