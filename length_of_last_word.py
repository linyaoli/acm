class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        n = 0
        while i >= 0:
            if s[i] == " ":
                if n != 0:
                    break
            else:
                n += 1
            i -= 1

        return n


sol = Solution()
print sol.lengthOfLastWord("   hello wor ld   ")
