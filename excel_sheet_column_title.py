"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ""
        while num > 26:
            remain = num % 26
            num = num / 26
            if remain == 0:
                num -=1
                remain = 26

            res = chr(remain + 64) + res

        res = chr(num + 64) + res

        return res

sol = Solution()
print sol.convertToTitle(104)
