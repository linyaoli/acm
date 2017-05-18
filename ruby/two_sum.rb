@param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  check_map = {}
  index1 = -100000
  index2 = -100000
  nums.each_with_index do |val, idx|
    p = target - val
    if check_map[p].nil?
      check_map[val] = idx
    else
      index1, index2 = idx, check_map[p]
      break
    end
  end

  if index1 > index2
    return index2, index1
  end
  return index1, index2
end
