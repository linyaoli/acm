class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        mapped = {}
        ret = 0
        cur = 0
        # each time while find a repeated character, we
        # move the pointer <cur> to the position after
        # the repeated character.
        # We renew the <ret> constantly, by <i - cur + 1>.
        for i in xrange(len(s)):
            if s[i] in mapped and mapped[s[i]] >= cur:
                cur = mapped[s[i]] + 1

            mapped[s[i]] = i
            ret = max(ret, i - cur + 1)

        return ret


s = Solution()
print s.lengthOfLongestSubstring("wlrbbmbmasdas")
