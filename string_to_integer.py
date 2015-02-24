class Solution:
    # @return an integer
    def atoi(self, str):
        if len(str) == 0 or str.isspace():
            return 0
        neg = 1
        ret = 0
        #skip leading white spaces
        i = 0
        for i in xrange(len(str)):
            if str[i] != " ": break
        #first non-whitespace char must be + - or digit
        if not str[i].isdigit() and str[i] not in ['+', '-']: return 0
        #after + - next char must be digit
        if str[i] in ['+', '-']:
            if not str[i+1].isdigit(): return 0
            if str[i] == '-': neg = -1
            i += 1

        for j in xrange(i, len(str)):
            if not str[j].isdigit():
                break
            ret = ret * 10 + int(str[j])
        ret *= neg
        if ret >= 0:
            return min(ret, 2**31 - 1)
        if ret < 0:
            return max(ret, -2**31)

sol = Solution()
print sol.atoi("      -11919730356x")
