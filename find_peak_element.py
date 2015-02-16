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
        start = 1
        end = len(num)
        if end == 0:
            return 0
        num = [-9223372036854775807] + num + [-9223372036854775807]
        while start <= end:
            mid = start + (end - start) / 2
            if num[mid] < num[mid + 1]:
                if num[mid+1] > num[mid+2]:
                    return mid
                else:
                    start = mid
            else:
                if num[mid-1] < num[mid]:
                    return mid - 1
                else:
                    end = mid

sol = Solution()
print sol.findPeakElement([1])
