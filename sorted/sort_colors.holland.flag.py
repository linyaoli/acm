class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        # r -> w -> b
        r = 0
        w = 0
        b = len(nums) - 1
        while w <= b:
            if nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            elif nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                w += 1
            else:
                w += 1

        return
