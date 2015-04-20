"""
Given a grid:

0 1 0
0 2 0
0 1 0

in which:
0 is a child, 1 is a policeman, 2 is a wall.

Output:
find the nearest police to each child (shown by distance).

1 0 1
2 x 2
1 0 1

"""
class Solution (object):
    def nearest(self, grid):
        # use BFS
        output_grid = [[9 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        for m in xrange(len(grid)):
            for n in xrange(len(grid[0])):
                if grid[m][n] == 1:
                    output_grid[m][n] = 0
                    queue = [(m, n)]
                    visited = [[False for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
                    k = 0
                    while queue != []:
                        tmp = []
                        while queue != []:
                            (i, j) = queue.pop(0)
                            if grid[i][j] == 2:
                                continue
                            if not visited[i][j]:
                                visited[i][j] = True
                                output_grid[i][j] = min(output_grid[i][j], k)
                            else:
                                continue
                            if i > 0:
                                tmp.append((i-1, j))
                            if i < len(grid) - 1:
                                tmp.append((i+1, j))
                            if j > 0:
                                tmp.append((i, j-1))
                            if j < len(grid[0]) - 1:
                                tmp.append((i, j+1))

                        if tmp != []:
                            k += 1
                            queue = tmp

                elif grid[m][n] == 2:
                    output_grid[m][n] = -1

        for i in xrange(len(output_grid)):
            for j in xrange(len(output_grid[0])):
                if output_grid[i][j] == 9:
                    output_grid[i][j] = -1

        return output_grid


sol = Solution()
a = [[0, 1, 0], [0, 2, 0], [0, 1, 0]]
aa = sol.nearest(a)
for i in range(3):
    print a[i], aa[i]
print
b = [[0, 2, 0], [0, 2, 0], [0, 2, 1]]
bb = sol.nearest(b)
for i in range(3):
    print b[i], bb[i]

print
b = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
bb = sol.nearest(b)
for i in range(3):
    print b[i], bb[i]
