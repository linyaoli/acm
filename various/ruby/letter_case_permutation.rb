# https://leetcode.com/problems/letter-case-permutation/description/
# @param {String} s
# @return {String[]}
def letter_case_permutation(s)
  res = []
  helper(s.split(""), 0, res)
  return res
end

def helper(s, j, res)
  if j == s.size
    res << s[0..-1].join("")
  else
    helper(s, j + 1, res)
    if s[j].swapcase != s[j]
      s[j].swapcase!
      helper(s, j + 1, res)
      s[j].swapcase!
    end
    # no difference
    # helper(s, j + 1, res)
  end
end

p letter_case_permutation("a1b2")
