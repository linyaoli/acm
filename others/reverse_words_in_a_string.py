class Solution:
# @param s, a string
# @return a string
    def reverseWords(self, s):
        # cp str to returned var
        s = s + " "
        s_cp = ""
        word = ""
        for letter in s:
            if letter != " ":
                word = word + letter
            elif letter == " " and word != "":
                if s_cp != "":
                    s_cp = word + " " + s_cp
                    word = ""
                else:
                    s_cp = word
                    word = ""

        return s_cp

sol = Solution()
s = "hello world!"
print sol.reverseWords(s)
