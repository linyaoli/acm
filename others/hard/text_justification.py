class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        cur = 0 # cur line length
        justified_words = []
        ret = []
        for word in words:
            if cur + len(word) > L:
                self.helper(justified_words, ret, L)
                cur = len(word) + 1
                justified_words = [word]
            elif cur + len(word) == L:
                justified_words.append(word)
                self.helper(justified_words, ret, L)
                cur = 0
                justified_words = []
            else:
                cur += len(word) + 1
                justified_words.append(word)
        if justified_words != []:#last line
            if cur < L:
                tmp = " ".join(justified_words)
                ret.append(tmp + " " * (L - len(tmp)))
            else:
                self.helper(justified_words, ret, L)

        return ret


    def helper(self, s, ret, L):
        tmp = ""
        n_all_words = 0
        if len(s) == 1:
            ret.append(s[0] + " " * (L - len(s[0])))
            return
        for word in s:
            n_all_words += len(word)
        n_spaces = (L - n_all_words) / (len(s) - 1)
        if_odd = (L - n_all_words) % (len(s) - 1)
        for i in xrange(len(s)):
            tmp += s[i]
            if if_odd != 0:
                tmp += " "
                if_odd -= 1
            if i != len(s) - 1:
                tmp += " " * n_spaces

        ret.append(tmp)

sol = Solution()
print sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print sol.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
print sol.fullJustify(["What","must","be","shall","be."], 12)
print sol.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)
