class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        res = 0
        mid = 0
        is_odd = 0
        for i in xrange(1, l - 1):
            tmp_res = 0
            for j in xrange(1, min(i, l - i - 1) + 1):
                if s[i + j] != s[i - j]:
                    break
                else:
                    tmp_res += 1
            if tmp_res > res:
                res = tmp_res
                mid = i
                is_odd = 1
            ######
            tmp_res = 0
            for j in xrange(1, min(i, l - i)):
                if s[i - j + 1] != s[i + j]:
                    break
                else:
                    tmp_res += 1
            if tmp_res > res:
                res = tmp_res
                mid = i
                is_odd = 0
        if is_odd == 1:
            return s[(mid - res):(mid + res + 1)]
        else:
            return s[(mid - res + 1):(mid + res + 1)]
        
