# https://leetcode.com/problems/2-keys-keyboard/description/
# @param {Integer} n
# @return {Integer}
def min_steps(n)
  ans = 0
  d = 2

  while n > 1
    while n % d == 0
      ans += d
      n /= d
    end

    d += 1
  end

  return ans
end

p min_steps(10)
p min_steps(2)
p min_steps(9)
