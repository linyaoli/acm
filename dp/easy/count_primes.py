"""
Count the number of prime numbers less than a non-negative number, n

"""
import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        lookup = [0] * n
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if lookup[i] == 1: continue
            for j in xrange(i**2, n, i):
                lookup[j] = 1
        print lookup
        return max(n - sum(lookup) - 2, 0)

sol = Solution()
print sol.countPrimes(16)
