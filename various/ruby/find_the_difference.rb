# https://leetcode.com/problems/find-the-difference/description/
# @param {String} s
# @param {String} t
# @return {Character}
def find_the_difference(s, t)
  s_chars = s.split("")
  t_chars = t.split("")
  s_chars += t_chars

  res = 0
  s_chars.each do |c|
    res ^= c.ord
  end

  return res.chr
end

# bit manipulation
p find_the_difference('abcd', 'abcde')
