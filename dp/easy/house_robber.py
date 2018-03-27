"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security
system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting
the police.

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        # brute force
        # choose at most n/2 elements
        # opt -> linear
        n = len(num)
        if n == 0: return 0
        if n <= 2: return max(num)
        val1 = num[0]
        val2 = max(num[0], num[1])
        for i in xrange(2, n):
            # which is larger?
            # num[i] + num[i-2] or num[i-1]
            val1, val2 = val2, max(val2, val1 + num[i])

        return val2

sol = Solution()
print sol.rob([1,2,3,4,5])
