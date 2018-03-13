# https://leetcode.com/problems/max-area-of-island/description/
# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
  res = 0
  grid.each_with_index do |a, i|
    grid[i].each_with_index do |b, j|
      if grid[i][j] == 1
        res = [res, helper(grid, i, j)].max
      end
    end
  end
  res
end

def helper(grid, i, j)
  return 0 if i == grid.size || j == grid[0].size ||
    i < 0 || j < 0 ||
    grid[i][j] == 0 || grid[i][j] == 2

  if grid[i][j] == 1
    grid[i][j] = 2
  end

  return 1 + helper(grid, i + 1, j) + helper(grid, i - 1, j) + helper(grid, i, j + 1) + helper(grid, i, j - 1)
end

p max_area_of_island([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]])

p max_area_of_island([[0,0,0,0,0,0,0,1]])
