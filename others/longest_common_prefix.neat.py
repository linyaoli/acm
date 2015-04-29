class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        min_n = 99999
        for str in strs:
            if len(str) < min_n:
                min_n = len(str)
        res = ""
        for i in xrange(min_n):
            one_char = strs[0][i]
            for j in xrange(1, len(strs)):
                if strs[j][i] == one_char:
                    continue
                else:
                    return res
            res += one_char

        return res

sol = Solution()
print sol.longestCommonPrefix(["b","cb","cab"])
