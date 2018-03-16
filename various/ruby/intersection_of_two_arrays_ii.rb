# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
  map = Hash.new
  map.default = 0
  nums1.each do |n|
    map[n] += 1
  end

  res = []
  nums2.each do |n|
    if map[n] > 0
      map[n] -= 1 
      res << n
    end
  end

  res
end

p intersect([1,2,2,1], [2,2])
