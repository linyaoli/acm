class Solution:
    # @return a string
    def getPermutation(self, n, k):
        nums = [0] * (n+1)
        count = 1
        for i in xrange(n):
            count *= i+1
            nums[i] = i+1

        k -= 1
        targetNum = ""
        for i in xrange(n):
            count /= n - i
            choosed = k / count
            print choosed
            targetNum += str(nums[choosed])
            for j in xrange(choosed, n-i):
                nums[j] = nums[j+1]
            k = k % count

        return targetNum


sol = Solution()
print sol.getPermutation(3, 5)
