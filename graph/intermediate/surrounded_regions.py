class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        xIdx = []
        yIdx = []
        #mark those 0s on the edge.
        for i in xrange(m):
            if board[i][0] == 'O':
                xIdx.append(i)
                yIdx.append(0)
            if board[i][n - 1] == 'O':
                xIdx.append(i)
                yIdx.append(n - 1)
        for i in xrange(n):
            if board[0][i] == 'O':
                xIdx.append(0)
                yIdx.append(i)
            if board[m - 1][i] == 'O':
                xIdx.append(m - 1)
                yIdx.append(i)

        k = 0
        #constantly traverse the table to mark all linked regions by 'Y'.
        while k < len(xIdx):
            x = xIdx[k]
            y = yIdx[k]
            board[x][y] = 'Y'
            if x > 0 and board[x - 1][y] == 'O':
                xIdx.append(x - 1)
                yIdx.append(y)
            if x < m - 1 and board[x + 1][y] == 'O':
                xIdx.append(x + 1)
                yIdx.append(y)
            if y > 0 and board[x][y - 1] == 'O':
                xIdx.append(x)
                yIdx.append(y - 1)
            if y < n - 1 and board[x][y + 1] == 'O':
                xIdx.append(x)
                yIdx.append(y + 1)
            k += 1
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
        print board



sol = Solution()
bod=[['x', 'x', 'x'], ['x', 'O', 'x'], ['x', 'x', 'x']]
sol.solve(bod)
