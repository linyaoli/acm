class Solution:
    # @return an integer
    def atoi(self, str):
        ret = 0
        isNeg = 1
        marked = False
        for i in xrange(len(str)):
            if str[i] == " " and not marked:
                continue
            if not str[i].isdigit():
                if str[i] == '-':
                    isNeg = -1
                if marked or str[i] not in ['-', '+']:
                    break
            else:
                ret = ret * 10 + int(str[i])
            marked = True
        if isNeg == 1:
            return min(ret, 2**31-1)
        else:
            return max(-ret, -2**31)


sol = Solution()
print sol.atoi("    b11228552307")
print sol.atoi("       -0123")
print sol.atoi(" 23a8f")
