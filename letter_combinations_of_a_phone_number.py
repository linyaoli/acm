class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        ret = []
        self.gen(0, ret, "", digits)
        return ret

    def gen(self, n, ret, chars, digits):
        if len(chars) == len(digits):
            ret.append(chars)
        else:
            for i in xrange(n, len(digits)):
                letters = self.helper(digits[i])
                for j in xrange(len(letters)):
                    chars += letters[j]
                    self.gen(i + 1, ret, chars, digits)
                    chars = chars[:-1]

    def helper(self, n):
        return {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            "0":" "
        }[n]

sol = Solution()
print sol.letterCombinations("23")
