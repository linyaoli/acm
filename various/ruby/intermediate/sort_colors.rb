# https://leetcode.com/problems/sort-colors/description/
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def sort_colors(nums)
  # r -> w -> b
  r = w = 0
  b = nums.size - 1

  while w <= b
    if nums[w] == 2
      nums[w], nums[b] = nums[b], nums[w]
      b -= 1
    elsif nums[w] == 0
      nums[w], nums[r] = nums[r], nums[w]
      r += 1
      w += 1
    else
      w += 1
    end
  end

  nums
end

p sort_colors([2,1,2,0,1,2,0,1,0])
