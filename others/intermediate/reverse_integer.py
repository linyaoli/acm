class Solution:
    # @return an integer
    def reverse(self, x):
        sum = 0
        _is_negative = False
        if x < 0:
            _is_negative = True
            x = -x
        while x > 0:
            if sum > 2**31/10:
                return 0
            sum = sum * 10 + x % 10
            x /= 10

        if _is_negative:
            sum = -sum
        return sum

class Solution:
    # @return an integer
    def reverse(self, x):
        ifneg = x < 0
        x = abs(x)
        ret = 0
        for i in xrange(len(str(x))):
            ret = ret * 10 + x % 10
            x /= 10
        if ifneg :
            return -ret
        return ret
