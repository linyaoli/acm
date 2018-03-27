class Solution:
    # @param {integer} n
    # @return {integer}
    res = 0
    def totalNQueens(self, n):
        A = [0] * n
        self.nqueens(A, 0)
        return self.res

    def match(self, A, r):
        for i in xrange(r):
            if A[i] == A[r] or abs(A[i] - A[r]) == r - i:
                return False
        return True

    def nqueens(self, A, i):
        if i == len(A):
            self.res += 1
        else:
            for j in xrange(len(A)):
                A[i] = j
                if self.match(A, i):
                    self.nqueens(A, i+1)
