class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # Rules:
        # every row is 1-9.
        # every column is 1-9.
        # every 3x3 board is 1-9.
        # The validation is about to find duplicates.
        # 1. every row and column

        for i in xrange(9):
            for j in xrange(9):
                for m in xrange(j+1, 9):
                    if (board[i][j] == board[i][m] and board[i][j].isdigit()) \
                        or (board[j][i] == board[m][i] and board[j][i].isdigit()):
                        return False

        # 3. every 3x3 board

        for i in xrange(3):
            for j in xrange(3):
                for m in xrange(9):
                    for n in xrange(m+1, 9):
                        if board[i * 3 + m / 3][j * 3 + m % 3] == board[i * 3 + n / 3][j * 3 + n % 3] \
                         and board[i * 3 + m / 3][j * 3 + m % 3].isdigit():
                            return False


        return True



sol = Solution()
print sol.isValidSudoku(["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."])
