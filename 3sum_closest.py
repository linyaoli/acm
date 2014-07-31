class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        MIN = 100000
        res = 0
        num.sort()
        n = len(num)
        for i in xrange(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                diff = abs(sum - target)
                if diff < MIN:
                    MIN = diff
                    res = sum
                if sum <= target:
                    j += 1
                else:
                    k -= 1

        return res
