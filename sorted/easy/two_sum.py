"""
if sorted: O(n)

if not sorted:
    brute: O(n^2), O(1)
    sort : O(nlogn)
    hash: O(n), O(n)
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num0 = num
        num = sorted(num)
        start = 0
        end = len(num) - 1
        while start < end:
            if num[start] + num[end] > target:
                end -= 1
            elif num[start] + num[end] < target:
                start += 1
            else:
                break
        fl = 0
        s = 0
        e = 0
        for i in xrange(len(num0)):
            if num0[i] == num[start]:
                s = i
        for i in xrange(len(num0)):
            if num0[i] == num[end] and i != s:
                e = i
        if s < e:
            return (s+1, e+1)
        else:
            return (e+1, s+1)

sol = Solution()
print sol.twoSum([5, 75, 25], 100)
