class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) == 0: return False
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if stack != []:
                    top = stack[-1]
                    if top == '(' and c == ')' or \
                        top == '[' and c == ']' or \
                        top == '{' and c == '}':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0

sol = Solution()
print sol.isValid('())((([{}]{})))')
