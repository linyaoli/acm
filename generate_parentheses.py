class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        lis = []
        self.gen(n, n, '', lis)
        return lis

    def gen(self, left, right, pair, lis):
        if left == 0:
            while right > 0:
                pair += ')'
                right -= 1
            lis.append(pair)
            return
        if right == 0:
            lis.append(pair)
            return
        self.gen(left - 1, right, pair + '(', lis)
        if left < right:
            self.gen(left, right - 1, pair + ')', lis)
        
