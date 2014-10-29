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
        _str = str
        str = ""
        for ch in _str:
            if ch != ' ':
                str += ch
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            is_negative = -1
            str = str[1:]
        final = 0
        for i in xrange(len(str)):
            final += (ord(str[i]) - ord('0')) * pow(10, len(str) - i - 1)

        final *= is_negative
        if final > 2147483647 or final < -2147483648:
            return 0
        return final
