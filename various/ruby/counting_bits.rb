# https://leetcode.com/problems/counting-bits/description/
# @param {Integer} num
# @return {Integer[]}
def count_bits(num)
  last_number_power_of_two = 2 # long var name explains well.
  result = Array.new(num + 1, 0)
  power_num = 1
  while power_num <= num
    result[power_num] = 1
    power_num *= 2
  end

  return result if num <= 2

  for i in 3..num
    if result[i] != 1
      result[i] = result[last_number_power_of_two] + result[i - last_number_power_of_two]
    else
      last_number_power_of_two = i
    end
  end

  result
end

p count_bits(0)
p count_bits(1)
p count_bits(2)
p count_bits(5)
p count_bits(10)
