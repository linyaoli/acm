"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        # find the largest num of factor 5.
        # then determine how many 5's before that.
        # obviously we know that 2's are more then 5's.
        n = max_five = (n / 5) * 5
        return self.saber(n)

    def saber(self, n):
        # how many 5's?
        num = 0
        n0 = n
        while n0 > 0:
            if n % 5 == 0:
                num += 1
                n = n / 5
            else:
                n0 -= 5
                n = n0
        return num

sol = Solution()
print sol.trailingZeroes(31)
