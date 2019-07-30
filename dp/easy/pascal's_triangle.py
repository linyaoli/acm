class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ret = []
        for n in xrange( numRows ):
            res = []
            for i in xrange(n/2 + 1):
                res.append( self.fac(n-i+1, n) / self.fac(1,i) )
            res += res[::-1]
            if n % 2 == 0:
                res.pop(len(res)/2)
            ret.append(res[:])

        return ret

    def fac(self, m, n):
        res = 1
        for i in xrange(m, n+1):
            res *= i
        return res
