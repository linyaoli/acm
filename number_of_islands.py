"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

11000
11000
00100
00011

return : 3

"""
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        n = 0
        ret = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '1':
                    ret.append(self.helper(grid, i, j))
                    n += 1

        return ret

    def helper(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) :
            return 0
        if grid[i][j] != '1':
            return 0
        grid[i][j] = 'X'
        return self.helper(grid, i-1, j) + \
        self.helper(grid, i+1, j) + \
        self.helper(grid, i, j-1) + \
        self.helper(grid, i, j+1) + 1

sol = Solution()
k = ['11000',
     '11000',
     '00100',
     '00011']
tmp = []
for i in k:
    tmp.append(list(i))

print sol.numIslands(tmp)
