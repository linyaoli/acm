class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        # any '0' connected with boarder '0' is not surrounded.
        # 1. located boarder '0'.
        self.board = []
        if len(board) == 0:
            return
        for i in board:
            self.board.append(list(i))

        boarder = []
        for i in xrange(len(board)):
            if board[i][0] == 'O':
                boarder.append([i, 0])
            if board[i][len(board[0]) - 1] == 'O':
                boarder.append([i, len(board[0]) - 1])

        for i in xrange(1, len(board[0]) - 1):
            if board[0][i] == 'O':
                boarder.append([0, i])
            if board[len(board) - 1][i] == 'O':
                boarder.append([len(board) - 1, i])

        for [i, j] in boarder:
            self.helper(i, j)
        for i in self.board:
            for j in xrange(len(i)):
                if i[j] == 'O':
                    i[j] = 'X'
                if i[j] == 'Y':
                    i[j] = 'O'
        return self.board

    def helper(self, i, j):
        if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]):
            return

        if self.board[i][j] == 'O':
            self.board[i][j] = 'Y'
        else:
            return

        self.helper(i + 1, j)
        self.helper(i - 1, j)
        self.helper(i, j + 1)
        self.helper(i, j - 1)

## This solution will exceed maximum recursion depth.


sol = Solution()
print sol.solve(["XOXOXO","OXOXOX","XOXOXO","OXOXOX"])
