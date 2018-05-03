# https://leetcode.com/problems/house-robber-ii
# # @param {Integer[]} nums
# @return {Integer}
def rob(nums)
  return 0 if nums.size == 0
  return nums.max if nums.size <= 2
  # rob from 0 to nums.size-2
  res1 = normal_rob(nums[0..-2])
  # rob from 1 to nums.size-1
  res2 = normal_rob(nums[1..-1])

  [res1, res2].max
end

def normal_rob(nums)
  dp = Array.new(nums.size, 0)
  dp[0] = nums[0]
  dp[1] = [dp[0], nums[1]].max
  for i in 2..nums.size-1
    dp[i] = [dp[i-2] + nums[i], dp[i-1]].max
  end

  dp[-1]
end

p rob([1,2,3,1])
p rob([2,3,2])
