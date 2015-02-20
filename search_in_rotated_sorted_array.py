class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid

            if A[mid] >= A[start]:
                if A[mid] > target and target >= A[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if A[mid] < target and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1


sol = Solution()
print sol.search([5, 1, 3], 3)
