def exist(board, word)
    @board = board
    @m = board.size
    @n = board[0].size
    @word = word

    @visited = Array.new(@m) { Array.new(@n, false) }

    for i in 0..@m-1
        for j in 0..@n-1
            return true if helper(i, j, 0, "") == true
        end
    end

    false
end

def helper(i, j, idx, cur)
    return true if cur == @word

    return false if i < 0 || j < 0 || i == @m || j == @n || idx == @word.size
    return false if @visited[i][j] == true 

    res = false

    if @board[i][j] == @word[idx]
        @visited[i][j] = true
        cur += @board[i][j]

        if (helper(i-1, j, idx+1, cur) == true || 
                helper(i+1, j, idx+1, cur) == true || 
                helper(i, j-1, idx+1, cur) == true || 
                helper(i, j+1, idx+1, cur) == true)
            return true
        end

        cur = cur[0..-2]
        @visited[i][j] = false
    end

    res
end

p exist([
    ['a', 'b', 'c', 'e'],
    ['s', 'f', 'c', 's'],
    ['a', 'd', 'e', 'e']
], 'abcced')
