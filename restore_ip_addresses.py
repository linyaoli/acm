class Solution:
    # @param s, a string
    # @return a list of strings

    def restoreIpAddresses(self, s):
        if len(s) > 12:
            return []
        sol = []
        self.validate(0, s, "", sol, 4)
        return sol

    def validate(self, k, s, res, sol, n):
        if n == 0 and k == len(s):
            sol.append(res[1:])

        for i in xrange(1, 4):
            if k + i <= len(s) and int(s[k : k + i]) < 256:
                if int(s[k : k + i]) >= 10 ** (i-1) or s[k : k + i] == "0":
                    res += '.' + s[k : k + i]
                    self.validate(k + i, s, res, sol, n-1)
                    res = res[:-i - 1]
