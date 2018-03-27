class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
      length = len(A)
      start = 0
      end = length - 1
      index1 = -1
      index2 = -1
      # find index1
      while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
          if mid == 0 or  A[mid - 1] != target:
            index1 = mid
            break
          else:
            end = mid - 1
        elif A[mid] > target:
          end = mid - 1
        elif A[mid] < target:
          start = mid + 1
      # find index2
      start = index1
      end = length - 1
      while start <= end:
        mid = (start + end) / 2
        if A[mid] == target:
          if mid == length - 1 or A[mid + 1] != target:
            index2 = mid
            break
          else:
            start = mid + 1
        else:
          end = mid - 1
      return [index1, index2]

sol = Solution()
print sol.searchRange([5, 7, 7, 8, 8, 10], 8)
