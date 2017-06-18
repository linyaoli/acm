# @param {Integer[]} nums
# @return {Integer}
# https://leetcode.com/problems/max-consecutive-ones/#/description
def find_max_consecutive_ones(nums)
  result = 0
  count = 0
  nums.each do |num|
    if num == 1
      count += 1
    else
      result = [count, result].max
      count = 0
    end
  end
  [result, count].max
end}
