# https://leetcode.com/problems/target-sum/description/
# @param {Integer[]} nums
# @param {Integer} s
# @return {Integer}
=begin
def find_target_sum_ways(nums, s)
  @nums = nums
  @s = s
  @res = []

  backtrack([], 0)
  @res.size
end

def backtrack(sol, n)
  if n == @nums.size
    sum = sol.inject(0, :+)
    @res << sol[0..-1] if sum == @s
  else
    for i in n..@nums.size-1
      sol << @nums[i]
      backtrack(sol, n + 1)

      sol[-1] *= -1
      backtrack(sol, n + 1)
      sol.pop
    end
  end
end
=end
# https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C++-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation
# basic idea:
# split nums into two subsets:
# positive set P, negative set N
# then we have :
# sum(P) - sum(N) = t
# SP = t + SN
# SP + SP = t + SP + SN, because SP + SN = nums,
# sum(P) = (t + nums) / 2
def find_target_sum_ways(nums, s)
  sum = nums.inject(0, :+)
  if sum < s || (s + sum) % 2 > 0
    return 0
  else
    return dp(nums, (s + sum) >> 1)
  end
end

def dp(nums, s)
  dp = Array.new(s + 1, 0)
  dp[0] = 1
  nums.each do |n|
    s.downto(n).each do |i|
      dp[i] += dp[i - n]
    end
  end
  dp[s]
end

p find_target_sum_ways([1, 1, 1, 1, 1], 3)
