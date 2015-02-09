class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) == 0:
            return False
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if stack != []:
                    top = stack[-1]
                    stack.pop()
                    if top == '(' and c == ')' or \
                        top == '[' and c == ']' or \
                        top == '{' and c == '}':
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True

sol = Solution()
print sol.isValid('()(([{}]{})))')
