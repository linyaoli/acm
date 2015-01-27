class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        count = [0 for _ in xrange(len(s))]

        count_0 = count_1 = 0
        count_2 = 1

        count_1 = self.check2(s[0], s[1]) + self.check1(s[0]) * self.check1(s[1])

        for i in xrange(2, len(s)):
            if self.check1(s[i]):
                count_0 += count_1
            if self.check2(s[i-1], s[i]):
                count_0 += count_2

            if count_0 == 0:
                return 0

            count_2 = count_1
            count_1 = count_0
            count_0 = 0

        return count_1

    def check1(self, a):
        if a == '0':
            return 0
        else:
            return 1

    def check2(self, a, b):
        if a == '1' or (a == '2' and int(b) in range(7)):
            return 1
        else:
            return 0

sol = Solution()
print sol.numDecodings("12120")
