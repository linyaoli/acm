# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
# @param {Integer[]} nums
# @return {Integer}
def find_unsorted_subarray(nums)
  # find numbers that are smaller than the largest on the left side. 
  left_max = -1000000
  left_index = 0
  nums.each_with_index do |n, i|
    left_index = [left_index, i].max if n < left_max
    left_max = [left_max, n].max
  end

  # find numbers that are larger than the smallest on the right side.
  right_min = 1000000
  right_index = nums.size - 1
  nums.each_with_index do |n, i|
    j = nums.size - i - 1
    right_index = [right_index, j].min if nums[j] > right_min
    right_min = [right_min, nums[j]].min
  end

  if left_index > right_index
    return left_index - right_index + 1
  else
    return 0
  end
end

p find_unsorted_subarray([1,2,3,4])
