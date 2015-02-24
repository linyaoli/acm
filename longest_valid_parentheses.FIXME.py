class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if s == '' or s == '(' or s == ')':
            return 0
        stack = [(-1, ')')]
        maxLen = 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1][1] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1][0])
            else:
                stack.append((i, s[i]))
        return maxLen

sol = Solution()
print sol.longestValidParentheses("()(())")
