# https://leetcode.com/problems/basic-calculator/description/
# # @param {String} s
# @return {Integer}
def calculate(s)
  s.delete!" "
  stack = []
  sign = 1
  n = 0
  result = 0

  for i in 0..s.size-1
    c = s[i]
    if numeric?(c)
      n  = 10 * n + c.to_i
    else
      case c
      when '+'
        result += sign * n
        n = 0
        sign = 1
      when '-'
        result += sign * n
        n = 0
        sign = -1
      when '('
        stack << result
        stack << sign
        sign = 1
        result = 0
      when ')'
        result += sign * n
        n = 0
        result *= stack.pop
        result += stack.pop
      end
    end
  end

  result += sign * n  if n != 0
  result
end

def numeric?(s)
  Float(s) != nil rescue false
end

p calculate("(1+(4+5+2)-3)+(6+8)+12")
p calculate(" 2-1 + 2 ")
p calculate("1+5-4")
p calculate("2-4-(8+2-6+(8+4-1+8-10))")
