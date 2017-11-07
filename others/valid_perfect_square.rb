# @param {Integer} num
# @return {Boolean}
def is_perfect_square(num)
    return true if num == 1
    s = 0
    e = num
    while e - s > 1
        m = (e + s) / 2
        if m**2 > num
            e = m
        elsif m**2 < num
            s = m
        else
            return true
        end
    end
    
    return false
end

p is_perfect_square(16)
