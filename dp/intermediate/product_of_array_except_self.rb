# https://leetcode.com/problems/product-of-array-except-self/description/
# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self1(nums)
  res1 = Array.new(nums.size, 1)
  (1..nums.size-1).each do |i|
    res1[i] = res1[i-1] * nums[i-1]
  end

  res2 = Array.new(nums.size, 1)
  (nums.size-2).downto(0).each do |i|
    res2[i] = res2[i+1] * nums[i+1]
  end

  res = []
  (0..nums.size-1).each do |i|
    res << res1[i] * res2[i]
  end

  res
end

# less space complexity
def product_except_self(nums)
  res = Array.new(nums.size, 1)
  (1..nums.size-1).each do |i|
    res[i] = res[i-1] * nums[i-1]
  end

  tmp = 1
  (nums.size-2).downto(0).each do |i|
    tmp *= nums[i+1]
    res[i] *= tmp
  end

  res
end

p product_except_self([1,2,3,4])
