"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        lookup = {}
        for i in num:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        cons = 1
        max = 1
        lookup = sorted(lookup)
        for i in xrange(1, len(lookup), 1):
            if lookup[i] - lookup[i-1] == 1:
                cons += 1
                if cons > max:
                  max = cons
            else:
                cons = 1
        return max
