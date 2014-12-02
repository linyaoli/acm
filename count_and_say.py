class Solution:
    # @return a string
    def countAndSay(self, n):
        count = 1
        say = "1"
        while count < n:
            print say
            last_char = say[0]
            tmp_say = ""
            tmp_count = 0
            for i in xrange(len(say)):
                if say[i] == last_char:
                    tmp_count += 1
                else:
                    tmp_say += str(tmp_count) + last_char
                    last_char = say[i]
                    tmp_count = 1
            tmp_say += str(tmp_count) + last_char
            last_char = say[i]
            tmp_count = 1
            say = tmp_say
            count += 1

        return say

sol = Solution()
print sol.countAndSay(10)
