=begin
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
=end
# ofcuz hash is a straight-forward solution.
def contains_nearby_duplicate(nums, k)
  len = nums.size
  return false if len < 2 || k < 1
  indexes = nums.map.with_index.sort.map(&:last)
  for i in 0..len-2
    if nums[indexes[i]] == nums[indexes[i+1]] && (indexes[i] - indexes[i+1]).abs <= k
      return true
    end
  end

  return false
end
