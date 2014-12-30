"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -inf.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Your solution should be in logarithmic complexity.

"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        start = 0
        end = len(num) - 1
        n = end
        if n == 0:
            return 0
        while start <= end:
            mid = start + (end - start) / 2
            if num[mid] < self.gen(num, mid + 1, n):
                if self.gen(num, mid + 1, n) > self.gen(num, mid + 2, n):
                    return mid + 1
                else:
                    start = mid
            else:
                if self.gen(num, mid - 1, n) < self.gen(num, mid, n):
                    return mid
                else:
                    end = mid

    def gen(self, num, i, n):
        if i > n:
            return -9223372036854775807
        if i < 0:
            return -9223372036854775807
        return num[i]

sol = Solution()
print sol.findPeakElement([1, 2])
