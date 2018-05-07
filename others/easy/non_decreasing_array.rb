# https://leetcode.com/problems/non-decreasing-array/description/
# @param {Integer[]} nums
# @return {Boolean}
def check_possibility(nums)
  1.upto(nums.size-1).each do |i|
    next if nums[i-1] <= nums[i]
    tmp = nums[i-1]
    nums[i-1] = nums[i]
    return true if is_sorted?(nums)
    nums[i-1] = nums[i] = tmp
    return is_sorted?(nums)
  end

  true
end

def is_sorted?(nums)
  0.upto(nums.size-2).each do |k|
    return false if nums[k] > nums[k+1]
  end
  true
end

p check_possibility([4,2,3])
p check_possibility([4,2,1])
p check_possibility([3,4,2,3])
p check_possibility([2,3,3,2,4])
p check_possibility([-1,4,2,3])
