# https://leetcode.com/problems/missing-number/description/
# # @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
  res = nums.size
  for i in 0..nums.size-1
    res ^= i ^ nums[i]
  end

  res
end

p missing_number([3,0,1])
p missing_number([9,6,4,2,3,5,7,0,1])
