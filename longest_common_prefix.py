class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        min_n = 99999
        for str in strs:
            min_n = min(min_n, len(str))
        res = ""
        for i in xrange(min_n):
            one_char = strs[0][i]
            for j in xrange(1, len(strs)):
                if strs[j][i] != one_char:
                    return res
            res += one_char

        return res


sol = Solution()
print sol.longestCommonPrefix(["123 sd12 1a", "123 sdasdasdasd"])
