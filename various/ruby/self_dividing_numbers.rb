# https://leetcode.com/problems/self-dividing-numbers/description/
#
# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def self_dividing_numbers(left, right)
  result = []

  while left <= right
    digits = get_digits(left)
    is_divisible = true

    digits.each do |digit|
      if digit == 0
        is_divisible = false
        break
      end
      is_divisible = false if left % digit != 0
    end

    result << left if is_divisible == true 
    left += 1
  end

  result
end

def get_digits(number)
  digits = []
  while number > 0
    digits << number % 10
    number /= 10
  end
  digits
end

p self_dividing_numbers(1, 22)
