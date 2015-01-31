class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def permute(self, num):
        return self.gen(num, 0)

    def gen(self, num, idx):
        res = []
        if idx == len(num):
            print num
            return
        for i in xrange(idx, len(num)):
            num[i], num[idx] = num[idx], num[i]
            self.gen(num, idx + 1)
            num[i], num[idx] = num[idx], num[i]

        return res

sol = Solution()
num = [1,2,3,4]
sol.permute(num)
