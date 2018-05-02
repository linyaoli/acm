# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
# # @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
  row_max = Array.new(grid.size, 0)
  column_max = Array.new(grid[0].size, 0)

  for i in 0..grid.size-1
    row_max[i] = grid[i].max
  end

  for i in 0..grid[0].size-1
    tmp = []
    for j in 0..grid.size-1
      tmp << grid[j][i]
    end

    column_max[i] = tmp.max
  end
  
  res = 0
  for i in 0..grid.size-1
    for j in 0..grid[i].size-1
      res += [row_max[i], column_max[j]].min - grid[i][j]
    end
  end

  res
end

p max_increase_keeping_skyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
