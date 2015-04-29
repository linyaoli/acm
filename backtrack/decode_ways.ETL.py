"""
'A' -> 1
'B' -> 2
...
'Z' -> 26

"""

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        self.count = 0
        self.gen(0, n, s)
        return self.count

    def gen(self, i, n, s):
        if i == n:
            self.count += 1
        else:
            for j in xrange(i + 1, min(i + 3,n + 1)):
                if int(s[i:j]) <= 26:
                    self.gen(j, n, s)


sol = Solution()
print sol.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
