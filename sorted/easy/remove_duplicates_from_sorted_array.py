class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 1: return len(A)
        i = 0
        for j in xrange(1, len(A)):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]

        return i + 1
