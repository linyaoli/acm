class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        len_a = len(haystack)
        len_b = len(needle)
        idx = 0
        if len_a < len_b:
          return None
        elif len_b == 0:
          return haystack
        else:
          while idx < len_a - len_b + 1:
            if haystack[idx] == needle[0]:
              i = 0
              for i in xrange(len_b):
                if haystack[i + idx] != needle[i]:
                  i = 0
                  break
              if i == len_b - 1:
                return haystack[idx:]

            idx += 1
s = Solution()
print s.strStr("mississippi", "issip")
