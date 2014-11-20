class MinStack:
    # @param x, an integer
    # @return an integer
    stk = []
    min_stk = []
    def push(self, x):
        self.stk.append(x)
        if len(self.min_stk) == 0 or self.min_stk[-1] >= x:
            self.min_stk.append(x)

    # @return nothing
    def pop(self):
        if len(self.stk) == 0:
            return
        rt = self.stk.pop()
        if len(self.min_stk) > 0 and rt == self.min_stk[-1]:
            self.min_stk.pop()

    # @return an integer
    def top(self):
        if len(self.stk) > 0:
            return self.stk[-1]
        else:
            #return -1
            #do nothing
            #FIXME should handle error
            pass
    # @return an integer
    def getMin(self):
        if len(self.min_stk) != 0:
            return self.min_stk[-1]
        pass



sol = MinStack()
sol.push(-1)
print sol.top()
print sol.getMin()
