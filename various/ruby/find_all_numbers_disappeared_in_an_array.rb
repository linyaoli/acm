# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# @param {Integer[]} nums
# @return {Integer[]}
def find_disappeared_numbers(nums)
  idx = 1

  while idx <= nums.size 
    if nums[idx-1] != idx &&  nums[idx-1] != nums[nums[idx-1]-1]
      tmp = nums[idx - 1]
      nums[idx - 1] = nums[tmp - 1]
      nums[tmp - 1] = tmp
    else
      idx += 1
    end
  end

  res = []
  p nums
  nums.each_with_index do |n, i|
    res << i + 1 if i != n - 1
  end
  res
end

p find_disappeared_numbers([4,3,2,7,8,2,3,1])
p find_disappeared_numbers([4,3,2,7,7,2,3,1])
