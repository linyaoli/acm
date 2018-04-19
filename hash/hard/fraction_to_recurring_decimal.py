"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

"""

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        isNeg = (numerator * denominator < 0)
        n1 = abs(numerator)
        n2 = abs(denominator)
        lst = []
        count = 0
        loop_dict = {}
        loop_str = None
        loop_start = 0

        while True:
            count += 1
            lst.append(str(n1 / n2))
            n1 = 10 * (n1 % n2)
            if n1 == 0 or n1 in loop_dict:
                break
            else:
                loop_dict[n1] = count 

        loop_str = "".join(lst[loop_dict[n1]:])

        res = lst[0]
        if len(lst) > 1:
            res += "."
        if loop_str:
            res += "".join(lst[1:len(lst) - len(loop_str)]) + "(" + loop_str + ")"
        else:
            res += "".join(lst[1:])

        if isNeg:
            res = "-" + res

        return res

sol = Solution()
print sol.fractionToDecimal(1,13)
print sol.fractionToDecimal(2,3)
