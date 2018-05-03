# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# # @param {Integer} s
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
  i = j = 0
  sum = 0
  min_length = nums.size + 1
  while j < nums.size
    sum += nums[j]
    j += 1

    while sum >= s 
      min_length = [min_length, j - i].min
      sum -= nums[i]
      i += 1
    end
  end

  if min_length == nums.size + 1
    return 0
  else
    return min_length
  end
end

p min_sub_array_len(7, [2,3,1,2,4,3])
