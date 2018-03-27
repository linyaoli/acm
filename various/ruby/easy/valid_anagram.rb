# https://leetcode.com/problems/valid-anagram/description/
# Given two strings s and t, write a function to determine if t is an anagram of s.
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
  base = {}
  base.default = 0
  s.each_char do |c|
    base[c] += 1
  end

  p base
  t.each_char do |c|
    base[c] -= 1
  end
  p base

  base.keys.each do |k|
    return false if base[k] != 0
  end

  true
end

p is_anagram('a', 'a')
