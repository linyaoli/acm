def word_break(s, word_dict)
    @s = s
    @word_dict = word_dict
    @sol = []

    return helper(0, [])
end

def helper(i, cur)
    if i == @s.size
        @sol << cur[0..-1]
        return true
    else
        for j in i..@s.size-1
            if @word_dict.include? @s[i..j]
                cur << @s[i..j]
                return true if helper(j+1, cur) == true
                cur.pop
            end
        end
    end

    false
end

p word_break("leetcode", ["leet", "code", "leetcode"])
