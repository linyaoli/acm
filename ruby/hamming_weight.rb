# @param {Integer} n, a positive integer
# @return {Integer}
# https://leetcode.com/problems/number-of-1-bits/#/description
def hamming_weight(n)
  count = 0
  while n > 0
    n &= n - 1
    count += 1
  end
  count
end
