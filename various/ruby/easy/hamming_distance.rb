# https://leetcode.com/problems/hamming-distance/description/

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def hamming_distance(x, y)
  x_bits = get_bits(x) 
  y_bits = get_bits(y)

  if x_bits.size > y_bits.size
    x_bits, y_bits = y_bits, x_bits
  end

  diff = 0
  i = 0
  while i < y_bits.size
    if i < x_bits.size
      diff += 1 if x_bits[i] != y_bits[i]
    else
      diff += 1 if y_bits[i] != 0
    end

    i += 1
  end

  diff
end

def get_bits(x)
  factor = 1
  bits = []
  while x > 0 
    bits << x % 2**factor
    x /= 2
  end

  bits
end

p hamming_distance(1, 4)

