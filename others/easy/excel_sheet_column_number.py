"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ret = 0
        for i in s:
            ret = (ord(i) - ord('A') + 1) + ret * 26
        return ret

sol = Solution()
print sol.titleToNumber('AAZ')
