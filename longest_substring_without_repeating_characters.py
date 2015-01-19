class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        m = 0
        n = 0
        lookup = [False for _ in xrange(256)]
        while n < len(s):
          if not lookup[ord(s[n])]:
            lookup[ord(s[n])] = True
            n += 1
          else:
            max_len = max(max_len, n - m)
            while s[m] != s[n]:
                lookup[ord(s[m])] = False
                m += 1
            m += 1
            n += 1

        return max(max_len, len(s) - m)

s = Solution()
print s.lengthOfLongestSubstring("wlrbbmbmasdas")
