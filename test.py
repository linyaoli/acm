class Solution:
    # @return an integer
    def reverse(self, x):
        if x > 2**31-1 or x < -2**31:
            return 0
        ifneg = x < 0
        x = abs(x)
        ret = 0
        for i in xrange(len(str(x))):
            ret = ret * 10 + x % 10
            x /= 10
        if ifneg :
            return -ret
        return ret



sol = Solution()
print sol.reverse(1534236469)
