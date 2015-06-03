'''
n = 3
123
132
213
231
312
321

k = 3
return '213'


cases of n == 3: n!

permutations: a1, a2, a3... an

assume

k1 = k,  a1 = k1/(n-1)!

further, we have:

a2 = k2/(n-2)!, k2 = k1 % (n-1)!
...
a(n-1) = k(n-1)/1!, k(n-1) = k(n-2) % 2!

an = k(n-1)


'''
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
            targetNum += str(nums[choosed]) + " "
            for j in xrange(choosed, n-i):
                nums[j] = nums[j+1]
            k = k % count

        return targetNum[:-1]


a = raw_input()
a = a.split(" ")
sol = Solution()
print sol.getPermutation(int(a[0]), int(a[1]))
