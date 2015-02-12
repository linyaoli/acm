class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        sup = 1
        i = len(digits) - 1
        while sup != 0 and i >= 0:
            digits[i] += sup
            if digits[i] >= 10:
                digits[i] %= 10
            else:
                sup = 0
            i -= 1
        if sup == 1:
            digits = [1] + digits
        return digits



s = Solution()
res = [9,9,9]
print s.plusOne(res)
