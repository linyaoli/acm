# https://leetcode.com/problems/add-digits/description/
# @param {Integer} num
# @return {Integer}
def add_digits(num)
  if num - 1 < 0
    return 1 + (num - 1) % -9
  else
    return 1 + (num - 1) % 9
  end    
end

p add_digits(38)
