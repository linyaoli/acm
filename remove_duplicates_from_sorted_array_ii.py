class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 2:
          return length
        prev = 1
        curr = 2
        while curr < length:
          if A[curr] == A[prev] and A[curr] == A[prev - 1]:
            curr += 1
          else:
            prev += 1
            A[prev] = A[curr]
            curr += 1

        return prev + 1
            
