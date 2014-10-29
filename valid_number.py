class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        #1st: remove all spaces.
        _s = s
        s = ""
        #2nd: find all those illegal characters.
        valid_set = {'1', '2', '3', '4', '5', \
            '6', '7', '8', '9', '0', '.', 'e', ' '  \
        }
        # count num of '.'
        count_dots = 0
        for ch in _s:
            if ch != ' ':
                s += ch
            if ch == '.':
                count_dots += 1
            if count_dots > 1:
                return False
            if ch not in valid_set:
                return False
        if s == '':
            return False

        #each number can be divided to two parts . ###e###
        head = ""
        tail = ""
        op = ""
        for i in xrange(len(s)):
            if s[i] == 'e' or s[i] == '.':
                head = s[:i]
                tail = s[i+1:]
                op = s[i]
                break
        if head == '' and tail == '' and op != '':
            return False
        if (head == '' or tail == '') and op == 'e':
            return False

        return self.helper(head) and self.helper(tail)


    def helper(self, s):
        head = ""
        tail = ""
        op = ""
        for i in xrange(len(s)):
            if s[i] == 'e' or s[i] == '.':
                head = s[:i]
                tail = s[i+1:]
                op = s[i]
                break
        if head == '' and tail == '' and op != '':
            return False
        if (head == '' or tail == '') and op == 'e':
            return False
        return True

sol = Solution()
print sol.isNumber("1e123")
