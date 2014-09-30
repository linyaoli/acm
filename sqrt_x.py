class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
      upper_bound = x
      lower_bound = 1
      while upper_bound - lower_bound > 1:
        if pow((upper_bound + lower_bound) / 2, 2) > x:
          upper_bound = (upper_bound + lower_bound) / 2
        elif pow((upper_bound + lower_bound) / 2, 2) < x:
          lower_bound = (upper_bound + lower_bound) / 2
        else:
          return (upper_bound + lower_bound) /2

      return (upper_bound + lower_bound) /2

s = Solution()
print s.sqrt(0)
