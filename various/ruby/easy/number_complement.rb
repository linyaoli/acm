# https://leetcode.com/problems/number-complement/description/
#
# @param {Integer} num
# @return {Integer}
def find_complement(num)
  bits = get_bits(num)
  complement = 0
  bits.each_with_index do |bit, i|
    complement += 2**i if bit == 0
  end

  complement
end

def get_bits(number)
  bits = []
  while number > 0
    bits << number % 2
    number /= 2
  end

  bits
end

p find_complement(1)
