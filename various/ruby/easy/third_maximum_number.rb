=begin
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
=end

# @param {Integer[]} nums
# @return {Integer}
def third_max(nums)
  max_min = -2**63
  max1 = max2 = max3 = max_min
  nums.uniq.each do |num|
    if num > max1
      max3, max2, max1 = max2, max1, num
    elsif num > max2
      max3, max2 = max2, num
    elsif num > max3
      max3 = num
    end
  end
  if max3 != max_min
    return max3
  end
  return max1
end
