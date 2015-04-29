class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        n1, n2 = len(a), len(b)
        a, b = list(a), list(b)
        for i in xrange(n2-1, -1, -1):
            if b[i] == a[n1-n2+i] == '0':
                continue
            elif b[i] == '0' or a[n1-n2+i] == '0':
                a[n1-n2+i] = '1'
            else:
                a[n1-n2+i] = '2'

        up = '0'
        for i in xrange(n1-1, -1, -1):
            if a[i] == '2':
                a[i] = '0' and up
                up = '1'
                continue
            if up == '1':
                if a[i] == '0':
                    a[i] = '1'
                    up = '0'
                else:
                    a[i] = '0'

        a = ''.join(a)
        if up == '1':
            a  = '1' + a
        return a
sol = Solution()
print sol.addBinary('1010', '1011')
