class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        ret = []
        self.helper(0, s, ret, [])
        return ret

    def helper(self, k, s, ret, sol):
        if k == len(s):
            ret.append(sol[:])
        else:
            for i in xrange(k, len(s)):
                if self.isPalindrome(s[k:i+1]):
                    sol.append(s[k:i+1])
                    self.helper(i+1, s, ret, sol)
                    sol.pop()

    def isPalindrome(self, s):
        for i in xrange(len(s)/2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


sol = Solution()
print sol.isPalindrome("ab")
print sol.partition("aab")
