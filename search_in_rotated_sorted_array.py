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
          if target == A[mid]:
            return mid
          if A[mid] >= A[start]:
              if target <= A[mid] and target >= A[start]:
                  end = mid - 1
              else:
                  start = mid + 1
          else:
              if target < A[mid] or target >= A[start]:
                  end = mid - 1
              else:
                  start = mid + 1

        return -1


sol = Solution()
print sol.search([3,1], 1)
