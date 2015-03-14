class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A == []: return 0
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            if mid > start and A[mid] > target and A[mid - 1] < target:
                return mid
            ###########################
            if A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def binarySearch(self, A, target):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            print A[start], A[end]
            if A[mid] < target:
                start = mid + 1
            elif A[mid] > target:
                end = mid - 1
            else:
                return mid

        return mid


    def searchInsert2(self, A, target):
        if A == []: return 0
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] > target:
                end = mid - 1
            elif A[mid] < target:
                start = mid + 1
            else:
                break
        if target > A[mid]: return mid + 1
        else: return mid



sol = Solution()
print sol.searchInsert([1,2,4,4,8,16,17], 17)
print sol.searchInsert2([1,2,4,4,8,16,17], 17)
