class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        for i in xrange(n):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > n or A[i] == A[A[i] -1]:
                    break;
                #A[i], A[A[i] - 1] = A[A[i] - 1], A[i]
                a = i
                b = A[i] - 1
                a, b = b, a
                A[a], A[b] = A[b], A[a]
        i = 0
        for i in xrange(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1
