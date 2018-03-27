class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        n1 = len(haystack)
        n2 = len(needle)
        for i in xrange(n1 - n2 + 1):
            if haystack[i : i + n2] == needle:
                return i
        return -1

s = Solution()
print s.strStr("mississippi", "issip")
print s.strStr("mississippi", "ip")
