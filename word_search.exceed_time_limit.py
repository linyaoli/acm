class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m = len(board) #3
        n = len(board[0])

        visited = [[0 for i in xrange(n)] for j in xrange(m)]
        res = False
        for i in xrange(m):
            for j in xrange(n):
                res = res or self.helper(visited, word, board, m, n, i, j, "")
                visited[i][j] = 0
                if res == True:
                    return True

        return res

    def helper(self, visited, word, board, m, n, i, j, saber):

        if i >= m or j >= n or i < 0 or j < 0:
            return False

        if visited[i][j] == 1:
            return False

        if len(saber) > len(word):
            return False

        if len(saber) > 0:
            if saber[-1] != word[len(saber) - 1]:
                return False

        visited[i][j] = 1
        saber += board[i][j]
        # the 1d input is fuckin ridiculous

        if saber == word:
            return True
        else:
            return self.helper(visited, word, board, m, n, i + 1, j, saber) or \
            self.helper(visited, word, board, m, n, i - 1, j, saber) or \
            self.helper(visited, word, board, m, n, i, j + 1, saber) or \
            self.helper(visited, word, board, m, n, i, j - 1, saber)

sol = Solution()

print sol.exist(["ab","cd"], "cdba")
