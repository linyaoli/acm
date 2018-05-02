# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
# # @param {Integer[]} nums
# @return {Integer}
def dominant_index(nums)
    idx = 0
    largest = second_largest = -1
    nums.each_with_index do |n, i|
        if n > largest
            second_largest = largest
            largest = n
            idx = i
        elsif n > second_largest
          second_largest = n
        end
    end
    p largest, second_largest

    if largest >= second_largest * 2
        return idx
    else
        return -1
    end

end

p dominant_index([0,0,3,2])
p dominant_index([0,0,0,1])
