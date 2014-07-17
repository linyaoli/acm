class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
      idx = 0
      length = len(A)
      for i in xrange(1, length):
        if A[i] == A[idx]:
          length -= 1
        else:
          idx += 1
        A[idx] = A[i]

      return length
