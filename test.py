class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        n = 9
        #check rows and columns
        for i in xrange(n):
            for j in xrange(n):
                for k in xrange(j + 1, n):
                    if board[i][j] == board[i][m] and board[i][j].isdigit() \
                        board[j][i] == board[m][i] and board[j][i].isdigit():
                        return False

        #check small boxes.
        n = 3
        for i in xrange(n):
            for j in xrange(n):
                for p in xrange(9):
                    for q in xrange(p+1, 9):
                        if board[i*3+p/3][j*3+p%3] == board[i*3+q/3][j*3+q%3]:
