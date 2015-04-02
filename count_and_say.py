class Solution:
    # @return a string
    def countAndSay(self, n):
        s = "1"
        for i in xrange(1, n):
            tmp = ""
            prev = s[0]
            count = 1
            for j in xrange(1, len(s)):
                if prev == s[j]:
                    count += 1
                else:
                    tmp += str(count) + prev
                    prev = s[j]
                    count = 1
            s = tmp + str(count) + prev
            print s

        return s

sol = Solution()
print sol.countAndSay(10)
