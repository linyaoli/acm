"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        # assume divisor is not zero.
        if dividend == 0:
            return 0
        ifNeg = (dividend < 0) ^ (divisor < 0)
        dd = abs(dividend)
        dv = abs(divisor)
        i = 0

        while dv < dd:
            dv = dv << 1
            i += 1
        res = 0

        while dd >= abs(divisor):
            if dd >= dv:
                dd -= dv
                res += 1 << i
            dv = dv >> 1
            i -= 1

        if ifNeg:
            return -res
        return min(res, 2147483647)

sol = Solution()
print sol.divide(-100, -3)
