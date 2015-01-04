class Solution:
    # @return a string
    def convert(self, s, nRows):
        if len(s) == 0 or nRows <= 0:
            return ""
        if nRows == 1:
            return s
        res = ""
        n = 2 * nRows - 2
        for i in xrange(nRows):
            for j in xrange(i, len(s), n):
                res += s[j]
                if i != 0 and i != nRows - 1 and j + n - 2 * i < len(s):
                    res += s[j + n - 2 * i]

        return res

sol = Solution()
print sol.convert("PAYPALISHIRING", 3)
