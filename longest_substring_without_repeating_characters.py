class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        lookup = {}
        maxlen = 0
        start = 0
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = i
            else:
                maxlen = max(maxlen, i - start)
                start = max(start, lookup[s[i]] + 1)
                lookup[s[i]] = i

        return max(maxlen, len(s)-start)

s = Solution()
print s.lengthOfLongestSubstring("wlrbbmbmasdas")
