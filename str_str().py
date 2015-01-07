class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        len_a = len(haystack)
        len_b = len(needle)
        idx = 0
        if len_a < len_b:
            return -1
        elif len_a == 0 or len_b == 0:
            return 0
        else:
            while idx <= len_a - len_b:
                for i in xrange(len_b):
                    if haystack[i + idx] != needle[i]:
                        i = 0
                        break
                    if i == len_b - 1:
                        #return haystack[idx:]
                        return idx
                idx += 1
            return -1

s = Solution()
print s.strStr("mississippi", "issip")
print s.strStr("mississippi", "ip")
