class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in xrange(1, 33):
            ret = ret * 2 + n % 2            
            n = n >> 1

        return ret


sol = Solution()
print sol.reverseBits(43261596)
