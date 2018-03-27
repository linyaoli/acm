"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
"""
#FIXME
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1:
            if nums == [0] : return 1
            else: return 0
        start = 0
        end = len(nums) - 2
        while start <= end:
            mid = (start + end) / 2
            if mid < nums[mid]:
                end = mid - 1
            elif mid > nums[mid]:
                start = mid + 1
            else:
                break

        return end + 1



sol = Solution()
print sol.missingNumber([0, 1])
