#
# Complete the minimum_number_of_steps function below.
#
def minimum_number_of_steps(floor)
    @MAX = 100000
    @n = floor.size
    @m = floor[0].size

    return -1 if floor[0][0] == 1 || floor[-1][-1] == 1

    visited = Array.new(@n) { Array.new(@m, 0) }
    @floor = floor
    res = trav(0, 0, visited)

    return -1 if res >= @MAX
    res
end

def trav(i, j, visited)
  return @MAX if (i < 0 || j < 0 || i >= @n || j >= @m) || @floor[i][j] == 1 || visited[i][j] == 1 
  return 0 if i == @n - 1 && j == @m - 1

  visited[i][j] = 1
  return [trav(i+1, j, visited), trav(i, j+1, visited), trav(i-1, j, visited), trav(i, j-1, visited)].min + 1
end


p minimum_number_of_steps([[0,0,0,0], [1,0,0,1], [0,0,1,0]])
p minimum_number_of_steps([[0,0,0,0], [1,1,1,1], [0,0,0,0]])
p minimum_number_of_steps([[0,0,0,0]])
p minimum_number_of_steps([[0,0,1,0], [1,0,0,0]])
p minimum_number_of_steps([[0,1,0,0], [0,0,1,0], [1,0,0,0]])
p minimum_number_of_steps([[0,1,0,0,0,0], [0,0,0,1,0,0], [1,1,0,1,0,0],[0,0,0,0,0,1],[0,0,1,0,0,0]])
p minimum_number_of_steps([
  [0,0,0,1,0,0,0],
  [1,1,0,1,0,1,0],
  [0,0,0,1,0,1,0],
  [1,0,1,1,0,1,0],
  [1,0,0,0,0,1,0]
])
