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
              if A[start] <= target and target <= A[mid]:
                  end = mid - 1
              else:
                  start = mid + 1
          else:
              if A[mid] >= target or target >= A[start]:
                  end = mid - 1
              else:
                  start = mid + 1
        return -1
