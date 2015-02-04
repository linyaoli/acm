"""
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        n = len(s)
        i = 0
        pre_n = 0 #num of chars before '.' or 'e'
        post_n = 0 # num of chars after
        isdot = ise = 0
        while i < n:
            ch = s[i]
            i += 1
            if ch.isdigit():
                if isdot == 1 or ise == 1:
                    post_n += 1
                else:
                    pre_n += 1
            else:
                if ch.isspace():
                    if isdot or ise:
                        if post_n == 0 or pre_n == 0:
                            return False
                    else:
                        if pre_n != 0:
                            return False
                elif ch == '.':
                    isdot += 1
                    if isdot > 1:
                        return False
                elif ch == 'e':
                    ise += 1
                    if ise > 1:
                        return False
                    if pre_n == 0:
                        return False
                elif ch in ['-', '+']:
                    if pre_n == 0 or (pre_n != 0 and post_n == 0):
                        continue
                    else:
                        return False
                else:
                    return False

        if pre_n == 0 and post_n == 0:
            return False

        if ise and (pre_n == 0 or post_n == 0):
            return False

        return True




sol = Solution()
print sol.isNumber(".1")
print sol.isNumber("3.")
print sol.isNumber(". 1")
print sol.isNumber("1 4")
