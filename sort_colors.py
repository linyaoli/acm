class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        length = len(A)
        m = 0
        n = length - 1
        idx = 0
        while idx < n + 1:
            if A[idx] == 0:
                A[m], A[idx] = A[idx], A[m]
                m += 1
                idx += 1
                continue
            if A[idx] == 2:
                A[n], A[idx] = A[idx], A[n]
                n -= 1
                continue
            idx += 1
