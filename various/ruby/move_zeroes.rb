# https://leetcode.com/problems/move-zeroes/description/
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
  idx = 0
  nums.each do |n|
    nums[idx] = n
    idx += 1 if n != 0
  end
  
  for i in idx..nums.size-1
    nums[i] = 0
  end

  nums
end

p move_zeroes([0, 1, 0, 3, 12])
