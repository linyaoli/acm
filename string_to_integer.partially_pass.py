class Solution:
    # @return an integer
    def atoi(self, str):
        if str == '':
            return 0
        if len(str) > 2:
            if str[:2] == '-+' or str[:2] == '+-':
                return 0
        is_negative = 1
        # remove all space
        # remove illegal chars, any num after illegal char will be discarded.
        _str = str
        str = ""
        for ch in _str:
            if ch != ' ':
                if (ch >= '0' and ch <= '9') or ch == '-' or ch == '+':
                    str += ch
                else:
                    break
        ###################
        if str == "" or str == '+' or str == '-':
            return 0

        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            is_negative = -1
            str = str[1:]
        if str[0] == '0':
            return 0
        final = 0
        for i in xrange(len(str)):
            final += (ord(str[i]) - ord('0')) * pow(10, len(str) - i - 1)
        # FIXME a issue lies within
        # consider the overflow in other language such as C / C++.
        # u cant compare a number with MAX & MIN_INT when it is overflow.
        # so in C/C++, u have to use long or long long.
        final *= is_negative
        if final > 2147483647 or final < -2147483648:
            return 0
        return final


sol = Solution()
print sol.atoi("-abc")
