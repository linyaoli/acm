class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def gen(self, x, n):
        if n == 0:
            return 1
        v = self.gen(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x
    def pow(self, x, n):
        if n < 0:
            return 1.0 / self.gen(x, -n)
        else:
            return self.gen(x, n)


sol = Solution()
print sol.pow(4, -2)
