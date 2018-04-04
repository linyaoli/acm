# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
  res = []
  nums.each_with_index do |n, i|
    if nums[n.abs - 1] < 0
      res << n.abs
    else
      nums[n.abs - 1] *= -1
    end
  end

  res
end

p find_duplicates([4, 3, 2, 7, 8, 2, 3, 1])
