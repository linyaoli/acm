# @param {Integer[][]} grid
# @return {Integer}
def island_perimeter(grid)
  @m = grid.size
  @n = grid[0].size
  result = 0
  for i in 0..@m-1
    for j in 0..@n-1
      result += number_of_surrounded(i, j, grid) if grid[i][j] == 1
    end
  end
  result
end

def number_of_surrounded(i, j, grid)
  result = 0
  result += 1 if !is_valid?(i-1, j) || grid[i-1][j] == 0
  result += 1 if !is_valid?(i, j-1) || grid[i][j-1] == 0
  result += 1 if !is_valid?(i+1, j) || grid[i+1][j] == 0
  result += 1 if !is_valid?(i, j+1) || grid[i][j+1] == 0
  result
end

def is_valid?(i, j)
  return false if i < 0 || i > @m-1 || j < 0 || j > @n-1 
  true
end

puts island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
