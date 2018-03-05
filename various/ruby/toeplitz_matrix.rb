# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
#
# @param {Integer[][]} matrix
# @return {Boolean}
# e.g.
# 1234
# 5123
# 9512
def is_toeplitz_matrix(matrix)
  m = matrix.size
  n = matrix[0].size

  for i in 0..n-1
    val = matrix[0][i]
    for j in 1..m-1
      if i + j < n && val != matrix[j][i + j]
        return false
      else
        next
      end
    end
  end

  for i in 0..m-1
    val = matrix[i][0]
    for j in 1..n-1
      if i + j < m && val != matrix[i + j][j]
        return false
      else
        next
      end
    end
  end

  true
end

p is_toeplitz_matrix([[1,2,3,4], [5,1,2,3], [9,5,1,2]])
p is_toeplitz_matrix([[1,2], [2,2]])
p is_toeplitz_matrix([[36,59,71,15,26,82,87],
                      [56,36,59,71,15,26,82],
                      [15, 0,36,59,71,15,26]])


