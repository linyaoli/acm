class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        for i in xrange(n):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > n or A[i] == A[A[i] -1]:
                    break;
                a = i
                b = A[i] - 1
                A[a], A[b] = A[b], A[a]

        for i in xrange(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1
