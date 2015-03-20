class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        for i in xrange(m):
            board[i] = list(board[i])

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = '0'
                    if self.gen(board, word, 1, i, j, m, n):
                        return True
                    board[i][j] = tmp
        return False

    def gen(self, board, word, k, i, j, m, n):
        if k == len(word):
            return True
        a = False
        if i - 1 >= 0 and board[i-1][j] == word[k]:
            tmp = board[i-1][j]
            board[i-1][j] = '0'
            a = a or self.gen(board, word, k + 1, i - 1, j, m, n)
            board[i-1][j] = tmp

        if a:
            return a

        if i + 1 < m and board[i+1][j] == word[k]:
            tmp = board[i+1][j]
            board[i+1][j] = '0'
            a = a or self.gen(board, word, k + 1, i + 1, j, m, n)
            board[i+1][j] = tmp

        if a:
            return a

        if j - 1 >= 0 and board[i][j-1] == word[k]:
            tmp = board[i][j-1]
            board[i][j-1] = '0'
            a = a or self.gen(board, word, k + 1, i, j - 1, m, n)
            board[i][j-1] = tmp

        if a:
            return a

        if j + 1 < n and board[i][j+1] == word[k]:
            tmp = board[i][j+1]
            board[i][j+1] = '0'
            a = a or self.gen(board, word, k + 1, i, j + 1, m, n)
            board[i][j+1] = tmp

        return a


b = [
  "ABCE",
  "SFCS",
  "ADEE"
]
sol = Solution()
print sol.exist(["aa"], "aa")
