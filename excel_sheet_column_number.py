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
        ls = list(s)
        res = 0
        print ls
        for i in xrange(len(ls) - 1, -1, -1):
            res += (ord(ls[i]) - ord('A') + 1) * pow(26, len(ls) - i - 1)

        return res

sol = Solution()
print sol.titleToNumber('AAZ')
