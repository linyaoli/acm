# @param {Integer[]} flowerbed
# @param {Integer} n
# @return {Boolean}
def can_place_flowers(flowerbed, n)    
    current = 0
    total = 0
    flowerbed = [0] + flowerbed + [0]
    flowerbed.each do |bed|
        if bed == 0
            current += 1
        else
            n -= (current + 1)/2 - 1
            current = 0
        end
        return true if n <= 0
    end
    n -= (current+1)/2 - 1
    return true if n <= 0
    return false
end
