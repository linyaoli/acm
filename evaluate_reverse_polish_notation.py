class Solution:
    def evalRPN(self, tokens):
        mock_stack = []
        operator_arr = ['+', '-', '*', '/']
        for token in tokens:
            if token == operator_arr[0]:
                mock_stack[-2] = float(mock_stack[-2]) + float(mock_stack[-1])
                mock_stack.pop(-1)
            elif token == operator_arr[1]:
                mock_stack[-2] = float(mock_stack[-2]) - float(mock_stack[-1])
                mock_stack.pop(-1)
            elif token == operator_arr[2]:
                mock_stack[-2] = float(mock_stack[-2]) * float(mock_stack[-1])
                mock_stack.pop(-1)
            elif token == operator_arr[3]:
                mock_stack[-2] = float(mock_stack[-2]) / float(mock_stack[-1])
                mock_stack[-2] = int(mock_stack[-2])
                mock_stack.pop(-1)
            else:
                mock_stack.append(token)
        return int(mock_stack[-1])

sol = Solution()
setter = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print sol.evalRPN(setter)
