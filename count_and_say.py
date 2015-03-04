class Solution:
    # @return a string
    def countAndSay(self, n):
        s = "1"
        for i in xrange(1, n):
            tmp = ""
            last = s[0]
            count = 1
            for j in xrange(1, len(s)):
                if last == s[j]:
                    count += 1
                else:
                    tmp += str(count) + last
                    last = s[j]
                    count = 1
            s = tmp + str(count) + last

        return s

sol = Solution()
print sol.countAndSay(10)
