"""
Question:
Given a string S, find the length of the longest substring T that contains at most two distinct characters.
For example,
Given S = "eceba",
T is "ece" which its length is 3.
"""
class Solution:
    def longestOfTwo(self, s):
        mapped = {}
        ret = 0
        cur = 0
        count = 0
        for i in xrange(len(s)):
            if s[i] not in mapped or mapped[s[i]] == 0:
                count += 1
                mapped[s[i]] = 0
            mapped[s[i]] += 1
            while count > 2:
                mapped[s[cur]] -= 1
                if mapped[s[cur]] == 0:
                    count -= 1
                cur += 1
            ret = max(ret, i - cur + 1)

        return ret

sol = Solution()
print sol.longestOfTwo("wlrbwlrbbmbmasdasbmbwlrbbmbwlrbbmbmasdasmasdasmasdas")
