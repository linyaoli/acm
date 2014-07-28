class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        if len(s) == 0:
            return False
        stack.append(s[0])
        for i in xrange(1, len(s), 1):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                continue
            if stack  != []:
              cur = stack[-1]
            else:
              cur = ''
            if s[i] == ')' and cur != '(':
                return False
            if s[i] == ']' and cur != '[':
                return False
            if s[i] == '}' and cur != '{':
                return False
            stack.pop()
        if len(stack) != 0:
            return False
        return True
