class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        n = 0
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == " ":
                if n > 0:
                    break
            else:
                n += 1

        return n


sol = Solution()
print sol.lengthOfLastWord("   hello wor ld   ")
