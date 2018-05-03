# https://leetcode.com/problems/longest-increasing-subsequence/description/
# # @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
  return 0 if nums.size == 0
  dp = Array.new(nums.size, 1)
  for i in 0..nums.size-1
    for j in 0..i-1
      if nums[i] > nums[j]
        dp[i] = [dp[i], dp[j] + 1].max
      end
    end
  end

  dp.max
end

p length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])
