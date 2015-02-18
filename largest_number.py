class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted(num, cmp=self.compare)
        tmp_res = ""
        for i in num:
            tmp_res += str(i)
        res = ""
        flag = False
        for i in xrange(len(tmp_res)):
            if tmp_res[i] == '0' and not flag:
                continue
            else:
                res += tmp_res[i]
                flag = True

        if not flag:
            res += '0'

        return res

    def compare(self, s1, s2):
        return (int(str(s2) + str(s1)) - int(str(s1) + str(s2)))




sol = Solution()
print sol.largestNumber([0, 0])
