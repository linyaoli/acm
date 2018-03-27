# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
  def guessNumber(self, n):
    s = 1
    e = n
    while s < e:
      anchor = (e - s) / 2 + s
      result = guess(anchor)
      if result == 1:
        s = anchor + 1
      else:
        e = anchor

    return s
