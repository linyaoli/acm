# https://leetcode.com/problems/generate-parentheses/
# @param {Integer} n
# @return {String[]}
def generate_parenthesis(n)
  @result = []
  generate(n, n, [])
  @result
end

def generate(l, r, pats)
  if l == 0 && r == 0
    @result << pats.join
  else
    if l > 0
      generate(l - 1, r, pats << '(')
      pats.pop
    end
    if l < r
      generate(l, r - 1, pats << ')')
      pats.pop
    end
  end
end

puts generate_parenthesis(4)
