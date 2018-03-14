# https://leetcode.com/problems/flood-fill/description/
# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} new_color
# @return {Integer[][]}
def flood_fill(image, sr, sc, new_color)
  @img = image
  @cur = image[sr][sc]
  @new = new_color
  return @img if @cur == @new
  fill(sr, sc)

  return @img
end

def fill(i, j)
  return if i < 0 || j < 0 || i == @img.size || j == @img[0].size
  return if @img[i][j] != @cur
  @img[i][j] = @new
  fill(i + 1, j)
  fill(i, j + 1)
  fill(i - 1, j)
  fill(i, j - 1)
end

p flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
p flood_fill([[0,0,0], [0,1,1]], 1, 1, 1)
