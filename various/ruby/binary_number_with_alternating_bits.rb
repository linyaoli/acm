# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
# @param {Integer} n
# @return {Boolean}
def has_alternating_bits(n)
    num = n ^ (n >> 1)
    (num & (num + 1)) == 0
end

p has_alternating_bits(10)
