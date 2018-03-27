class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        #backtrack
        self.helper(board, 0, 0)
        print board

    def helper(self, board, i, j):
        if j >= 9:
            return self.helper(board, i + 1, 0)
        if i == 9:
            return True
        if board[i][j] == '.':
            for k in xrange(1,10):
                board[i][j] = str(k)
                if self.check(board, i, j):
                    if self.helper(board, i, j+1):
                        return True
                board[i][j] = '.'
        else:
            return self.helper(board, i, j+1)

        return False

    def check(self, board, i, j):
        for k in xrange(9):
            if k != j and board[i][k] == board[i][j]:
                return False
            if k != i and board[k][j] == board[i][j]:
                return False
        for r in xrange(i/3*3, i/3*3+3, 1):
            for c in xrange(j/3*3, j/3*3+3, 1):
                if (r != i or c != j) and board[r][c] == board[i][j]:
                    return False

        return True

sol = Solution()
a = []
for i in ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]:
    a.append(list(i))

sol.solveSudoku(a)
