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
