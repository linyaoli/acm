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
        hashtable = {}
        ret = 1
        for i in num:
            hashtable[i] = 1
        for i in num:
            left = i - 1
            right = i + 1
            count = 1
            while left in hashtable:
                count += 1
                del hashtable[left]
                left -= 1
            while right in hashtable:
                count += 1
                del hashtable[right]
                right += 1
            ret = max(count, ret)
            print hashtable

        return ret
        """
        lookup = {}
        for i in num:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        cons = 1
        max = 1
        lookup = sorted(lookup)
        print lookup
        for i in xrange(1, len(lookup)):
            if lookup[i] - lookup[i-1] == 1:
                cons += 1
                if cons > max:
                  max = cons
            else:
                cons = 1
        return max
        """

sol = Solution()
print sol.longestConsecutive([100,4,200,1, 1,3,2,5,7,6, 101,102])
