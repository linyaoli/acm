# https://leetcode.com/problems/single-number-iii/description/
# @param {Integer[]} nums
# @return {Integer[]}
# apparently we can use hash table, but the requirements are:
# linear time complexity, constant space complexity.
# solution: https://leetcode.com/problems/single-number-iii/discuss/68901/Sharing-explanation-of-the-solution.
# this is fucking annoying.
def single_number(nums)
  val = 0
  nums.each { |num| val ^= num }
  bit = val & ~(val - 1)
  num1 = num2 = 0
  nums.each do |num|
    if num & bit > 0
      num1 ^= num
    else
      num2 ^= num
    end
  end

  return [num1, num2]

end

#p single_number([1,2,1,3,2,5])
p single_number([1,2,2,3,4,1])
