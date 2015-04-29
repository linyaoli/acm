#This is an optimized solution using KMP.
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        i = 0
        ptable = self.kmp(needle)
        while i <= len(haystack) - len(needle):
            for j in xrange(len(needle)):
                if haystack[i + j] != needle[j]:
                    i += max(j - ptable[j - 1], 1)
                    break
            else:
                return i
        return -1

    def kmp(self, needle):
        #build the kmp-match table.
        prefix = set()
        postfix = set()
        ret = [0]
        for i in xrange(1, len(needle)):
            prefix.add(needle[:i])
            postfix = {needle[j:i+1] for j in xrange(1, i+1)}
            ret.append(len((prefix & postfix or {''}).pop()))
        return ret

s = Solution()
print s.strStr("mississippi", "issip")
print s.strStr("mississippi", "is")
