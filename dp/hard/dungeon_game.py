"""
Solution:
Start from the end point, back to the first point.
In each grid, we find the minimum requirement to go to the next right or next down.

State transaction:

cur(i, j) = max(1, min(cur(i+1, j), cur(i, j+1)) - dungeon(i, j))
cur(-1, -1) = max(1, 1 - dungeon(-1, -1))


"""
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        # each grid has to maintain a minimum needed hp.
        # Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
        n = len(dungeon)
        if n == 0:
            return 0
        m = len(dungeon[0])
        lr = [[0 for _ in xrange(m)] for _ in xrange(n)] # least required
        # lr[i][j] = max(1, min(lr[i+1][j], lr[i][j+1]) - dungeon[i][j])
        if dungeon[-1][-1] >= 0:
            lr[-1][-1] = 1
        else:
            lr[-1][-1] = 1 - dungeon[-1][-1]

        for i in xrange(n-2, -1, -1):
            lr[i][m-1] = max(lr[i+1][m-1] - dungeon[i][m-1], 1)

        for i in xrange(m-2, -1, -1):
            lr[n-1][i] = max(lr[n-1][i+1] - dungeon[n-1][i], 1)

        for i in xrange(n-2, -1, -1):
            for j in xrange(m-2, -1, -1):
                lr[i][j] = max(1, min(lr[i+1][j], lr[i][j+1])-dungeon[i][j])

        return lr[0][0]



sol = Solution()
print sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
