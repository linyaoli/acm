"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
      n = 0
      N = x
      if x < 0:
        return False
      while x > 0:
        x /= 10
        n += 1
      return self.gen(N, n - 1)

    def gen(self, x, i):
      if i < 1:
        return True
      left_remain = x % pow(10, i)
      left = x / pow(10, i)
      right = x % 10

      if left != right:
        return False
      else:
        return self.gen(left_remain/10, i - 2)
"""
# so actually, recursion does use extra space(stack).
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        # n digits
        n = 0
        _x = x
        while _x > 0:
            _x /= 10
            n += 1
        i = 1
        while  i <= n / 2:
            right = x % 10
            left = x / pow(10, n - i * 2 + 1)
            if right != left:
                return False
            else:
                x -= right + left * pow(10, n - i * 2 + 1)
                x /= 10
                i += 1

        return True

sol = Solution()
print sol.isPalindrome(2222222)
