class Solution:
    # @param s, a string
    # @return a list of strings

    def restoreIpAddresses(self, s):
        res = []
        sol = []
        if len(s) > 12 or len(s) < 4:
            return []
        self.helper(s, 4, sol, "", res)
        return res

    def helper(self, s, n, res, item, _res):
        # illegal format: exceed maximum length = 3 or > 255.
        if len(s) > 3 * n:
            return
        if item != "":
            if int(item) > 255:
                return
        else:
            if n != 4:
                return
        if n == 0:
            _res.append(res)
            print res
        else:
            for i in xrange(1, 4):
                res.append(s[:i])
                self.helper(s[i:], n - 1, res, s[:i], _res)
                res.pop()
        


sol = Solution()
print sol.restoreIpAddresses("25525511135")
