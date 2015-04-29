class Solution:
    # @return a list of integers
    def grayCode(self, n):
        # The nth code is reversed code of (n-1)th code, plus 1 << n.
        res = [0]
        for i in xrange(0, n):
            shift = 1 << i
            # reverse the code of (n-1)th
            for j in xrange(len(res) - 1, -1, -1):
                res.append(res[j] + shift)

        return res


sol = Solution()
print sol.grayCode(3)
