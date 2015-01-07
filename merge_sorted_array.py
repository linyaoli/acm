class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        len_a = m - 1
        len_b = n - 1
        i = m + n - 1
        while i >= 0 and len_b >= 0:
            if len_a < 0 or A[len_a] <= B[len_b]:
                A[i] = B[len_b]
                len_b -= 1
            else:
                A[i] = A[len_a]
                len_a -=1
            i -= 1
        return
