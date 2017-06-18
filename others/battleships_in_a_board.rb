# @param {Character[][]} board
# @return {Integer}
def count_battleships(board)
  m = board.size
  n = board[0].size
  res = 0
  (0..m-1).each do |i|
    (0..n-1).each do |j|
      if i + 1 < m && j + 1 < n
        res += 1 if board[i+1][j] == '.' && board[i][j+1] == '.' && board[i][j] == 'X'
      else
        if (i + 1 == m && j + 1 < n && board[i][j+1] == '.' && board[i][j] == 'X') ||
          (i + 1 < m && j + 1 == n && board[i+1][j] == '.' && board[i][j] == 'X') || 
          (i + 1 == m && j + 1 == n && board[i][j] == 'X')
          res += 1
        end
      end
    end
  end
  res
end
