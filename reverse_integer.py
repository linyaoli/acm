class Solution:
    # @return an integer
    def reverse(self, x):
        sum = 0
        _is_negative = False
        if x < 0:
            _is_negative = True
            x = -x

        while x >= 10:
            sum = (sum + x % 10) * 10
            x /= 10
        sum += x
        if _is_negative:
            sum = -sum

        return sum 
