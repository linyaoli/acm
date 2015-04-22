class Block:
    def match (self, n):
        ret = []
        sol = []
        self.helper(n, n, ret, sol)
        return ret

    def helper (self, l, r, ret, sol):
        if l == 0 and r == 0:
            #while r > 0:
            #    sol += "e"
            #    r -= 1
            #ret.append(''.join(sol[:]))
            #print sol
            print sol[:]
        else:
            if l > 0:
                sol.append("if")
                self.helper(l - 1, r, ret, sol)
                sol.pop()
            if l < r:
                sol.append("endif")
                self.helper(l, r - 1, ret, sol)
                sol.pop()
blk = Block()
print blk.match(3)
