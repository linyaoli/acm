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
        sum = 0
        for idx in range(len(s)):
            if idx > 0 and self.atoi(s[idx]) > self.atoi(s[idx-1]):
                sum += self.atoi(s[idx]) - self.atoi(s[idx-1]) * 2
            else:
                sum += self.atoi(s[idx])
        return sum



        
