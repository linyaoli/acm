class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        up = 1
        for i in xrange(len(digits)-1, -1, -1):
            if up == 0:
                break
            up, digits[i] = (digits[i] + up) / 10, (digits[i] + up ) % 10

        if up == 1:
            digits = [1] + digits

        return digits


s = Solution()
res = [0,9,9]
print s.plusOne(res)
