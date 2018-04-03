# @param {Integer[][]} nums
# @param {Integer} r
# @param {Integer} c
# @return {Integer[][]}
# https://leetcode.com/problems/reshape-the-matrix/#/description
def matrix_reshape(nums, r, c)
  return nums if r * c != nums.size * nums[0].size
  result_matrix = []
  new_row = []
  nums.each do |row|
    row.each do |entry|
      new_row << entry
      if new_row.size == c
        result_matrix << new_row
        new_row = []
      end
    end
  end
  result_matrix
end
