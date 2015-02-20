class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        up = 1
        for i in xrange(len(digits)-1, -1, -1):
            _t = digits[i] + up
            up, digits[i] = _t / 10, _t % 10
        if up == 1:
            digits = [1] + digits

        return digits


s = Solution()
res = [9,9,9]
print s.plusOne(res)
