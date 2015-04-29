class Solution:
    # @return an integer
    # I, II, III
    # V 5
    # X 10
    # L 50
    # C 100
    # D 500
    # M 1000
    def atoi(self, c):
        return {
        'I': 1,
        'V': 5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }[c]

    def romanToInt(self, s):
        ret = self.atoi(s[0])
        for i in xrange(1, len(s)):
            ret += self.atoi(s[i])
            if self.atoi(s[i]) > self.atoi(s[i-1]):
                ret -= 2 * self.atoi(s[i-1])
        return ret

        
