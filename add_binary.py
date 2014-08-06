class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        na = len(a)
        nb = len(b)
        upper = 0
        n = max(na, nb)
        a = a[::-1]
        b = b[::-1]
        c = ""
        for i in xrange(n):
            ai = 0
            bi = 0
            if i < na:
                ai = int(a[i]) - int('0')
            if i < nb:
                bi = int(b[i]) - int('0')
            lower = (ai + bi + upper) % 2
            upper = (ai + bi + upper) / 2
            c = str(int('0') + lower) + c
        if upper == 1:
            c = '1' + c
        return c
