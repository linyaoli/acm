"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted(num, cmp=self.compare)
        res = ""
        for i in num: res += str(i)
        return res.lstrip('0') or '0'

    def compare(self, s1, s2):
        return (int(str(s2) + str(s1)) - int(str(s1) + str(s2)))



""" An elegant solution
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a]
"""



sol = Solution()
print sol.largestNumber([0, 10])
