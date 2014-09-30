class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        _len = 0
        lookup = {}
        for idx in xrange(len(s)):
          _len += 1
          if s[idx] not in lookup:
            lookup[s[idx]] = idx
          else:
            _len = idx - lookup[s[idx]]
            for i in lookup:
              if lookup[i] < lookup[s[idx]]:
                lookup[i] = lookup[s[idx]]
            print _len, lookup
            #print lookup[s[idx]]
            lookup[s[idx]] = idx

            #print s[idx - _len : idx]

          if _len > max_len:
            max_len = _len
          #print max_len

        return max_len

s = Solution()
print s.lengthOfLongestSubstring("wlrbbmbmasdas")
