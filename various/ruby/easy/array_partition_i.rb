# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
  nums.sort!
  res = 0
  nums.each_slice(2).each do |pair|
    res += pair[0]
  end

  res
end}
