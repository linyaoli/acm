class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        #remove all non-alphanumic chas
        _len = len(s)
        _s = ""
        for idx in xrange(_len):
            if s[idx].isdigit() is True or s[idx].isalpha() is True:
                _s += s[idx].lower()
        if _s == "":
            return True
        #check
        _len = len(_s)
        for x in xrange(_len / 2):
          if _s[x] != _s[_len - 1 - x]:
            return False

        return True
