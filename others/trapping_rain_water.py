class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        length = len(A)
        idx = [0] * length
        high = 0 # highest bar
        trapped = 0
        for i in xrange(length):
            idx[i] = high
            if A[i] > high:
                high = A[i]
        high = 0
        for i in xrange(length - 1, -1, -1):
            tmp = min(high, idx[i])
            if tmp < A[i]:
                idx[i] = 0
            else:
                idx[i] = tmp - A[i]
            if A[i] > high:
                high = A[i]
            trapped += idx[i]
        return trapped
