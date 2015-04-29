"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.m_stack = []

    def push(self, x):
        self.stack.append(x)
        if self.m_stack == [] or self.m_stack[-1] >= x:
            self.m_stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack == []:
            return
        poped = self.stack[-1]
        self.stack.pop()
        if self.m_stack != [] and poped == self.m_stack[-1]:
            self.m_stack.pop()

    # @return an integer
    def top(self):
        if self.stack != []:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if self.m_stack != []:
            return self.m_stack[-1]

sol = MinStack()
sol.push(-1)
print sol.top(), sol.getMin()
