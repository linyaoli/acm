class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        saber = 0 # parenthese count
        maxi = 0 # final result, this has to be an even num
        current_maxi = [0 for i in xrange(len(s))] # temp maximum
        for idx in xrange(len(s)):
            if s[idx] == '(':
                saber += 1
            else:
                if saber - 1 < 0:
                    current_maxi[idx] = 0
                else:
                    saber -= 1
                    current_maxi[idx] = 2

        last_two = -1 # if there are more than one zero between
        tmp_maxi = 0
        for idx in xrange(len(s)):
            if current_maxi[idx] == 2:
                if idx - last_two > 2: # illegal pair
                    tmp_maxi = 2
                else:
                    tmp_maxi += current_maxi[idx]
                if tmp_maxi > maxi:
                    maxi = tmp_maxi
                last_two = idx
        print current_maxi
        return maxi


sol = Solution()
print sol.longestValidParentheses("()(())")
