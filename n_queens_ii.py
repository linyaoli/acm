class Solution:
    # @return an integer
    res = 0
    def totalNQueens(self, n):
        A = [0] * n
        self.nqueens(A, 0, n)
        return self.res

    def check(self, A, r):
        for i in xrange(r):
            if A[i] == A[r] or abs(A[i] - A[r]) == r - i :
                return False
        return True

    def nqueens(self, A, cur, n) :
        if cur == n:
            self.res += 1
            return
        else:
            for i in xrange(n):
                A[cur] = i
                if self.check(A, cur):
                    self.nqueens(A, cur + 1, n)


         
