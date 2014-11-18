class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        max_local = A[0]
        min_local = A[0]
        res = A[0]
        for i in xrange(1, len(A)):
            max_cp = max_local
            # A[i] * min_local : in case that A[i] < 0 and min_local < 0 makes a greater value
            max_local = max(A[i] * max_local, A[i], A[i] * min_local)
            min_local = min(A[i] * max_cp, A[i], A[i] * min_local)
            res = max(res, max_local)

        return res
