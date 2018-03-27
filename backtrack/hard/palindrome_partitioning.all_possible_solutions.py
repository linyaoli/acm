class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.res = []
        self.helper(0, s, [])
        return self.res

    def check(self, s):
        ed = len(s) - 1
        st = 0
        while st < ed:
            if s[st] != s[ed]:
                return False
            st += 1
            ed -= 1

        return True

    def helper(self, i, s, sub):
        n = len(s)
        if i == n:
            self.res.append(sub[:])
            return

        for k in xrange(i, n):
            if self.check(s[i: k + 1]):
                sub.append(s[i: k + 1])
                self.helper(k + 1, s, sub)
                sub.pop()


sol = Solution()
print sol.partition("aab")
