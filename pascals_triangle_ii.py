class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = self.generate( rowIndex + 1 )
        return res[-1]

    def factorial(self, n):
        res = 1
        for i in xrange(1, n + 1):
            res *= i
        return res

    def generate(self, numRows):
        n = numRows
        res = []
        for i in xrange(0, n):
            res_ = []
            for j in xrange(0, i+1):
                res_.append( self.factorial(i)/(self.factorial(j) * self.factorial(i-j)) )
            res.append(res_)
        return res
        
