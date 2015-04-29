class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        n = len(nums)
        s = 0
        e = n - 1
        while s <= e:
            m = (e - s) / 2 + s
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                if nums[m-1] == target:
                    e -= 1
                else:
                    return m
        return -1
