"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new

place for his thievery so that he will not get too much attention. This time,

all houses at this place are arranged in a circle. That means the first house

is the neighbor of the last one. Meanwhile, the security system for these houses

remain the same as for those in the previous street.

********************************************************************************

Given a list of non-negative integers representing the amount of money of each

house, determine the maximum amount of money you can rob tonight without alerting the police.


"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n <= 2: return max(nums)
        val1 = nums[0]
        val2 = max(nums[0], nums[1])

        for i in xrange(2, n):
            # which is larger?
            # num[i] + num[i-2] or num[i-1]
            val1, val2 = val2, max(val2, val1 + nums[i])

        kmax = val2
        nums += nums
        val1 = nums[0]
        val2 = max(nums[0], nums[1])
        for i in xrange(2, 2*n):
            # which is larger?
            # num[i] + num[i-2] or num[i-1]
            val1, val2 = val2, max(val2, val1 + nums[i])

        return val2 - kmax


sol = Solution()
print sol.rob([1,2,3,4,5])
