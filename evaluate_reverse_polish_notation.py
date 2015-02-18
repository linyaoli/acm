class Solution:
    def evalRPN(self, tokens):
        mock_stack = []
        for token in tokens:
            k = token
            if token in ['+', '-', '*', '/']:                
                m = mock_stack.pop()
                n = mock_stack.pop()
                if token == '+':
                    k = m + n
                elif token == '-':
                    k = n - m
                elif token == '*':
                    k = m * n
                elif token == '/':
                    k = int(float(n) / float(m))
            mock_stack.append(int(k))

        return mock_stack[0]

sol = Solution()
setter = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print sol.evalRPN(setter)
