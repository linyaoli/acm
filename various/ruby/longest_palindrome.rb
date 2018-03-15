# https://leetcode.com/problems/longest-palindrome/description/
# @param {String} s
# @return {Integer}
def longest_palindrome(s)
  map = Hash.new
  map.default = 0
  s.each_char do |c|
    map[c] += 1
  end

  res = 0
  has_one = false
  map.keys.each do |k| 
    has_one = true if map[k] % 2 == 1
    res += map[k] / 2 if map[k] >= 2
  end

  res *= 2
  res += 1 if has_one
  res
end

p longest_palindrome("abccccdd")
