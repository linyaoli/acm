# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
# https://leetcode.com/problems/combination-sum-iv/#/description
def combination_sum4_1(nums, target)
  return 0 if nums.size == 0 || target < 0
  return 1 if target == 0

  ret = 0
  @mapper ||= {}
  return @mapper[target] if @mapper[target]

  for i in 0..nums.size-1
    ret += combination_sum4(nums, target - nums[i])
  end

  @mapper[target] = ret
  ret
end

# for the life of me I cannot figure this out.
def combination_sum4(nums, target)
  nums, sols = nums.sort, [1] + [0] * target
  for i in 0..target
    nums.each do |num|
      break if num > i
      sols[i] += 1 if num == i
      sols[i] += sols[i - num] if num < i
    end
  end

  sols[target]
end

p combination_sum4([1,2,3], 4)
p combination_sum4([1,5], 200)
p combination_sum4([1,2], 89)
p combination_sum4([3,33,333], 10000)
