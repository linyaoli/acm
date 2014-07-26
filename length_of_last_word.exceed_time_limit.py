class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == "" or s == " ":
            return 0
        if len(s) == 1:
          return 1
        last_space = 0
        i = 0
        for i in xrange(len(s)):
            print last_space
            if s[i] == ' ':
                last_space = i

        return i - last_space
