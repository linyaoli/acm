#!/usr/bin/python


class Solution:
    def singleNumber(self, A):
        res = int(0)
        _len = len(A)
        MAX_INT = 2147483647
        for inBit in range(0, 32, 1):
            count = 0
            for inElem in range(0, _len, 1):
                count = count + ((A[inElem] >> inBit) & 1)
            res = res | ((count % 3) << inBit)

            if res > MAX_INT:
                return res - (MAX_INT + 1) * 2

        return res

sol = Solution()
A = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
B = [-2, -2, -2, 3, 3, 3, 1]
print sol.singleNumber(A)
