class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        self.k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1)

    def quickSelect(self, nums, left, right):
        if left == right : return nums[left]
        pivotIndex = right
        pivotIndex = self.partition(nums, left, right, pivotIndex)
        if pivotIndex == self.k:
            return nums[pivotIndex]
        elif self.k < pivotIndex:
            return self.quickSelect(nums, left, pivotIndex-1)
        else:
            return self.quickSelect(nums, pivotIndex + 1, right)

    def partition(self, nums, left, right, pivot):
        p_val = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        storeIndex = left
        for i in xrange(left, right):
            if nums[i] < p_val:
                nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                storeIndex += 1
        nums[right], nums[storeIndex] = nums[storeIndex], nums[right]
        return storeIndex


sol = Solution()
print sol.findKthLargest([2,1], 1)
