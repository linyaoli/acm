class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        n = len(s)
        if n == 0 or n == 1:
            return s
        # reverse the whole string and remove trailing spaces.
        # [::-1]
        r_s = ""
        last_letter = ""
        for i in s:
            if i != " " or (i == " " and last_letter != " "):
                r_s = i + r_s
            last_letter = i
        if r_s[0] == " ":
            r_s = r_s[1:]
        n = len(r_s)

        # reverse r_s by word
        r_w = ""
        i = 0
        while i < n:
            # find the start of the word
            while i < n and r_s[i] == " ":
                r_w += r_s[i]
                i += 1
            start = i
            # find the end of the word
            while i < n and r_s[i] != " ":
                i += 1
            end = i
            # reverse by word
            for k in xrange(end - 1, start - 1, -1):
                r_w += r_s[k]

        return r_w

sol = Solution()
print sol.reverseWords("       the        sky is     b lue      ")
