# @param {Integer} n
# @return {String[]}
# https://leetcode.com/problems/fizz-buzz/#/description
def fizz_buzz(n)
  result = []
  for i in 1..n
    if i % 3 == 0 && i % 5 == 0
      result << "FizzBuzz"
    elsif i % 3 == 0
      result << "Fizz"
    elsif i % 5 == 0
      result << "Buzz"
    else
      result << i.to_s
    end
  end
  result
end
