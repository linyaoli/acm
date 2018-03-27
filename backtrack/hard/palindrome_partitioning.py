class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.ret = []
        self.helper(0, s, [])
        return self.ret

    def helper(self, k, s, sol):
        if k == len(s):
            self.ret.append(sol[:])
        else:
            for i in xrange(k, len(s)):
                if self.isPalindrome(s[k:i+1]):
                    sol.append(s[k:i+1])
                    self.helper(i+1, s, sol)
                    sol.pop()

    def isPalindrome(self, s):
        for i in xrange(len(s)/2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


sol = Solution()
print sol.isPalindrome("ab")
print sol.partition("aab")
