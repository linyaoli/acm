#this solution is ultimately optimized to reduce time cost.
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = []
        n = rowIndex
        for i in xrange(0, n/2 + 1):
            res.append( self.fac(n-i+1, n) / self.fac(1,i) )
        res += res[::-1]
        if n % 2 == 0:
            res.pop(len(res)/2)

        return res

    def fac(self, m, n):
        res = 1
        for i in xrange(m, n+1):
            res *= i
        return res

sol = Solution()
print sol.getRow(0)
