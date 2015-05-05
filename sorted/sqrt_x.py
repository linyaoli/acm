class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
      upper = x
      lower = 1
      while upper - lower > 1:
        if pow((upper + lower) / 2, 2) > x:
          upper = (upper + lower) / 2
        elif pow((upper + lower) / 2, 2) < x:
          lower = (upper + lower) / 2
        else:
          return (upper + lower) /2

      return (upper + lower) /2

s = Solution()
print s.sqrt(300)
