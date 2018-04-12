# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
# # @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_partition_k_subsets(nums, k)
  @target = nums.sum / k
  @nums = nums.sort
  @res = []

  return false if @nums[-1] > @target
  while @nums && @nums[-1] == @target
    @nums.pop
    k -= 1
  end

  gen([0] * k)
end

def gen(remain)
  return true if @nums == []
  val = @nums.pop
  remain.each_with_index do |v, i|
    if v + val <= @target
      remain[i] += val
      return true if gen(remain) == true
      remain[i] -= val
    end
    break if remain.nil?
  end
  @nums << val
  false
end

p can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 6)
p can_partition_k_subsets([1,1,1,1,1,1,1,1,1,1], 5)
