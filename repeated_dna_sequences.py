class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        ret = {}
        for i in xrange(len(s) - 9):
            if s[i:i+10] in ret:
                ret[s[i:i+10]] += 1
            else:
                ret[s[i:i+10]] = 1
        res = []
        for i in ret.keys():
            if ret[i] > 1:
                res.append(i)
        return res


sol = Solution()
print sol.findRepeatedDnaSequences("AAAAAAAAAAA")
