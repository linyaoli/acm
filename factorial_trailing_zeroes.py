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
        num = 0
        while n > 0:
            n = n / 5
            num += n
        return num
        
sol = Solution()
print sol.trailingZeroes(18085483)
