# https://leetcode.com/problems/basic-calculator-ii/description/
# # @param {String} s
# @return {Integer}
def calculate(s)
  s.delete!" "
  sets = s.split(/([+\-*\/])/)

  numbers = []
  operators = []
  sign = 1

  sets.each do |n|
    if numeric?(n)
      numbers << sign * n.to_i
      sign = 1
      while operators[-1] == "*" || operators[-1] == "/"
        op = operators.pop
        b = numbers.pop
        a = numbers.pop
        if op == "*"
          numbers << a * b
        else
          numbers << (1.0*a/b).to_i
        end
      end
    else
      operators << n
      sign = -1 if n == "-"
    end
  end
  p numbers
  p operators

  numbers.inject(0) {|sum, x| sum + x}
end

def numeric?(s)
  Float(s) != nil rescue false
end

#p calculate("1 3+5 / 2 * 13")
#p calculate("3/2")
#p calculate("1+1+1")
#p calculate("1+1-1")
p calculate("14-3/2")

