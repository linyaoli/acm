"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        # assume divisor is not zero.
        assert divisor != 0
        if dividend == 0: return 0
        ifNeg = (dividend < 0) ^ (divisor < 0)
        # a / b
        a = abs(dividend)
        b = abs(divisor)
        i = 0

        while b < a:
            b = b * 2
            i += 1
        
        ret = 0
        while a >= abs(divisor):
            if a >= b:
                print a, b
                a -= b
                ret += 1 << i
            b = b / 2
            i -= 1

        if ifNeg: return -ret
        return min(ret, 2147483647)

sol = Solution()
print sol.divide(100, 3)
