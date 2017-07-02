# @param {Integer[]} nums
# @return {Integer}
# https://leetcode.com/problems/missing-number/#/description
def missing_number(nums)
  res = 0
  for i in 0..nums.size
    res ^= i
  end
  nums.each do |num|
    res ^= num
  end
  res
end
