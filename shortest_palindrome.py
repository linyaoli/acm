class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):


    def shortestPalindrome_ETL(self, s):
        k = s
        s = list(s)
        rs = s[::-1]
        i = len(s)
        while i > 0:
            j = 0
            for j in xrange(i):
                if s[j] != rs[j]:
                    i -= 1
                    rs.pop(0)
                    break
            if j == i - 1:
                break
        return k[i:][::-1] + k

sol = Solution()
print sol.shortestPalindrome("aacecaaa")
print sol.shortestPalindrome("abcd")
print sol.shortestPalindrome("lileeyao")
#print sol.shortestPalindrome("eaae")
