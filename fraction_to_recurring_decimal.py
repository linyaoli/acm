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
        n1 = numerator
        n2 = denominator
        if n2 == 0:
            return False
        if n1 == 0:
            return 0

        if n1 % n2 == 0:
            return str(n1 / n2)
        else:
            remain = abs(n1) % abs(n2)
            if abs(n1) < abs(n2):
                remain = n1
            decimal = self.saber(abs(remain), abs(n2))
            if float(n1) / n2 < 0 and int(float(n1) / n2) == 0:
                return "-0." + decimal
            else:
                return str(int(float(n1) / n2 )) + "." + decimal

    def saber(self, num, den):
        #FIXME
        #round up >= 0.^5, no need ?
        #determine where it ends.
        res = []
        startParenthess = 0
        looped = False
        while True:
            remain = int((num * 10) / den)
            num = (num * 10) % den

            if remain not in res:
                res.append(remain)
            else:
                for i in xrange(len(res)):
                    if res[i] == remain:
                        startParenthess = i
                break

        ret = ""
        ret_2 = ""
        if res[-1] == 0:
            res.pop()

        for i in xrange(len(res)):
            if i < startParenthess :
                ret += str(res[i])
            else:
                ret_2 += str(res[i])
        if ret_2 == "":
            return ret
        else:
            return ret + "(" + ret_2 + ")"

sol = Solution()
print sol.fractionToDecimal(1,333)
