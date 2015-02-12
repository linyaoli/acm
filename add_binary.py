class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        n1 = len(a) - 1
        n2 = len(b) - 1
        a = list(a)
        b = list(b)
        sup = 0
        while n2 >= 0:
            tmp = int(a[n1]) ^ int(b[n2]) ^ sup#remain
            sup = (int(a[n1]) + int(b[n2]) + sup) / 2#increase
            a[n1] = str(tmp)
            n1 -= 1
            n2 -= 1
        while n1 >= 0:
            if sup == 1:
                tmp = (int(a[n1]) + sup) % 2
                sup = (int(a[n1]) + sup) / 2
                a[n1] = str(tmp)
                n1 -= 1
            else:
                break
        if sup == 1:
            return '1' + "".join(a)
        else:
            return "".join(a)


sol = Solution()
print sol.addBinary("1", "1")
