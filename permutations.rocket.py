class Solution:
    # @return a string
    def getPermutation(self, n, k):
        nums = [0] * (n+1)
        count = 1
        for i in xrange(n):
            count *= i+1
            nums[i] = i+1

        # find maximum f(p)
        max_fp = 0

        k -= 1
        targetNum = []
        res = []
        for i in xrange(n):
            count /= n - i
            choosed = k / count
            targetNum.append(nums[choosed])
            for j in xrange(choosed, n-i):
                nums[j] = nums[j+1]
            k = k % count
        

        return targetNum[:-1]


a = raw_input()
a = a.split(" ")
sol = Solution()
print sol.getPermutation(int(a[0]), int(a[1]))
