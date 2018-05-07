# https://leetcode.com/problems/01-matrix/description/
# @param {Integer[][]} matrix
# @return {Integer[][]}
=begin
def update_matrix(matrix)
  @distance = Array.new(matrix.size) { Array.new(matrix[0].size, 0) }
  @visited = Array.new(matrix.size) { Array.new(matrix[0].size, false) }

  @matrix = matrix
  @matrix.each_with_index do |col, i|
    col.each_with_index do |entry, j|
      @distance[i][j] = search(i, j, 0) if entry == 1
    end
  end

  @distance 
end

def search(i, j, dist)
  return 0 if i < 0 || i == @matrix.size || j < 0 || j == @matrix[0].size
  return 0 if @visited[i][j] == true
  return dist if @matrix[i][j] == 0

  @visited[i][j] = true

  res = [
    search(i+1, j, dist+1),
    search(i, j+1, dist+1),
    search(i-1, j, dist+1),
    search(i, j-1, dist+1)
  ].compact

  res.select!{|d| d > 0}

  @visited[i][j] = false
  return res.min
end
=end

def update_matrix(matrix)
  dist = Array.new(matrix.size) { Array.new(matrix[0].size, 0) }
  matrix.each_with_index do |col, i|
    col.each_with_index do |entry, j|
      if entry == 0 
        dist[i][j] = 0
      else
        top = left = 10000
        top = dist[i-1][j] if i > 0
        left = dist[i][j-1] if j > 0
        dist[i][j] = [10000, left + 1, top + 1].min
      end
    end
  end
  matrix.each_with_index do |col, m|
    col.each_with_index do |r, n|
      i = matrix.size - m - 1
      j = col.size - n - 1
      if dist[i][j] != 0 && dist[i][j] != 1
        down = right = 10000
        down = dist[i+1][j] if i < matrix.size-1 
        right = dist[i][j+1] if j < matrix[0].size-1
        dist[i][j] = [dist[i][j], down + 1, right + 1].min
      end
    end
  end

  dist
end
p update_matrix([[0],[0],[0],[0],[0]])

p update_matrix(
  [
    [1,1,0],
    [1,1,1],
    [1,1,1]
  ]
)
