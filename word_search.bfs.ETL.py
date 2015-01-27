class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(board) == 0:
            return False

        m = len(board)#3
        n = len(board[0])#4

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[0 for _ in xrange(n)] for _ in xrange(m)]
                    queue = [(i, j, 1)]
                    visited[i][j] = 1
                    while queue != []:
                        (a, b, k) = queue.pop(0)
                        if k == len(word):
                            return True
                        visited[a][b] = 1

                        if a - 1 >= 0 and visited[a-1][b] == 0:
                            if word[k] == board[a-1][b]:
                                queue.append((a-1,b, k+1))

                        if b - 1 >= 0 and visited[a][b-1] == 0:
                            if word[k] == board[a][b-1]:
                                queue.append((a, b-1, k+1))

                        if a + 1 < m and visited[a+1][b] == 0:
                            if word[k] == board[a+1][b]:
                                queue.append((a+1, b, k+1))

                        if b + 1 < n and visited[a][b+1] == 0:
                            if word[k] == board[a][b+1]:
                                queue.append((a, b+1, k+1))

        return False

sol = Solution()
b = [
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]

print sol.exist([['a', 'a']], "aa")
