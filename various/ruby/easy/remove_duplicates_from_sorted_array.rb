# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return nums if nums.size <= 1
  j = 0
  for i in 1..nums.size-1
    if nums[i] != nums[j]
      j += 1
      nums[j] = nums[i]
    end
  end

  nums
end

p remove_duplicates([1,1,1,2,3,3,4,4,5])
