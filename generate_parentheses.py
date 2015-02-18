class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        ret = []
        self.helper(n, n, ret, "")
        return ret

    def helper(self, l, r, ret, str):
        if l == 0:
            while r > 0:
                str += ')'
                r -= 1
            ret.append(str)
        else:
            if l > 0:
                str += '('
                self.helper(l-1, r, ret, str)
                str = str[:-1]
            if l < r:
                str += ')'
                self.helper(l, r-1, ret, str)
                str = str[:-1]

sol = Solution()
print sol.generateParenthesis(3)
