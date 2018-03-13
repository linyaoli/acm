# https://leetcode.com/problems/count-binary-substrings/description/
# @param {String} s
# @return {Integer}
def count_binary_substrings(s)
  prev = 0
  cur = 1
  res = 0

  for i in 1..s.size-1
    if s[i] == s[i-1]
      cur += 1
    else
      prev = cur
      cur = 1
    end

    res += 1 if prev >= cur
  end

  res
end

p count_binary_substrings("00110011")
p count_binary_substrings("10101")
