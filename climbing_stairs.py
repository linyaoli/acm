class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        count = [0] * n
        if n <= 2:
            return n
        count[0] = 1
        count[1] = 2
        for idx in xrange(2, n):
            count[idx] = count[idx-1] + count[idx-2]

        return count[n-1]

    def climbStairs(self, n):
        if n < 3: return n
        a = 1
        b = 2
        ret = 0
        for i in xrange(2, n):
            ret = a + b
            a = b
            b = ret

        return ret
