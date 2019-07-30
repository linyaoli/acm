class Solution:
    # @return a string
    def atoi(self, c):
      return {
        'I': 1,
        'V': 5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }[c]
    def intToRoman(self, num):
      result = []
      symbol = [ 'I','V','X', 'L','C', 'D','M']
      scale = 1000
      for i in xrange(6, -1, -2):
        digit = num / scale
        if digit != 0:
            if digit <= 3:
              result.append(symbol[i] * digit)
            elif digit == 4:
              result.append(symbol[i])
              result.append(symbol[i+1])
            elif digit == 5:
              result.append(symbol[i+1])
            elif digit <= 8:
              result.append(symbol[i+1])
              result.append(symbol[i] * (digit-5))
            elif digit == 9:
              result.append(symbol[i])
              result.append(symbol[i+2])
        num = num % scale
        scale /= 10

      res = ""
      for i in result:
          res += i
      return res


sol = Solution()
print sol.intToRoman(9)
