class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        sup = 0
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        else:
            digits[-1] %= 10
            sup = 1
        for i in xrange(len(digits) - 2, -1, -1):
            digits[i] += sup
            if digits[i] >= 10:
                digits[i] %= 10
                continue
            else:
                sup = 0
                break
        if sup == 1:
          digits.insert(0, 1)
        return digits



s = Solution()
res = [9,9,9]
print s.plusOne(res)
