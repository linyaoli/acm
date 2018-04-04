# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# @param {Integer[]} cost
# @return {Integer}
def min_cost_climbing_stairs(cost)
  dp = Array.new(cost.size, 0)
  dp[0], dp[1] = cost[0], cost[1]

  for i in 2..cost.size-1
    dp[i] = [dp[i-2], dp[i-1]].min + cost[i]
  end

  [dp[-2], dp[-1]].min
end

p min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
p min_cost_climbing_stairs([10, 15, 20])
