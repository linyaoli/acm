class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0        
        max_local = min_local = res = A[0]
        for i in xrange(1, len(A)):
            # A[i] * min_local : in case that A[i] < 0 and min_local < 0 makes a greater value
            max_local, min_local = max(A[i] * max_local, A[i], A[i] * min_local), \
                min(A[i] * max_local,    A[i], A[i] * min_local)
            res = max(res, max_local)

        return res


sol = Solution()
print sol.maxProduct([2,3,-2,4])
