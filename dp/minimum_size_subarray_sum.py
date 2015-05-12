"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum >= s.
If there isn't one, return 0 instead.


For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

"""

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if nums == []: return 0
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        for i in xrange(1, n):
            sums[i] = sums[i-1] + nums[i]
        if sums[-1] < s: return 0
        j = 0
        length = n
        for i in xrange(n):
            while j < i and sums[i] - sums[j] >= s:
                j += 1
            if sums[i] - sums[j] + sums[j] >= s:
                length = min(length, i - j + 1)

        return length

sol = Solution()
print sol.minSubArrayLen(7, [2,3,1,2,4,3])
print sol.minSubArrayLen(5, [2,3,1,1,1,1,1])
print sol.minSubArrayLen(4, [1,4,4])
