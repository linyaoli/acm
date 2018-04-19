# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  return false if matrix == [] || matrix == [[]]
  return false if target < matrix[0][0] || target > matrix[-1][-1]

  col = matrix[0].size - 1
  row = 0 

  while col >= 0 && row <= matrix.size-1
    if target == matrix[row][col]
      return true
    elsif target < matrix[row][col]
      col -= 1
    else
      row += 1
    end
  end

  false
end

p search_matrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 18)
