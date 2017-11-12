class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def permute(self, num):
        res = []
        self.gen(num, 0, res)
        return res, len(res)

    def gen(self, num, i, res):
        if i == len(num) - 1:
            res.append(num[:])
        else:
            for j in xrange(i, len(num)):
                num[j], num[i] = num[i], num[j]
                self.gen(num, i+1, res)
                num[j], num[i] = num[i], num[j]
    # check the difference
    # this is a wrong solution
    def gen2(self, num, i, res):
        if i == len(num) - 1:
            res.append(num[:])
        else:
            for j in xrange(i, len(num)):
                num[j], num[i] = num[i], num[j]
                # swap num[i] and every element after it.
                self.gen(num, j+1, res)
                num[j], num[i] = num[i], num[j]

sol = Solution()
num = [1,2,3]
print sol.permute(num)
