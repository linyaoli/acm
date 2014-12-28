"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2  times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = 1
        major_num = num[0]

        for i in xrange(1, len(num)):
            if count == 0:
                major_num = num[i]
            if num[i] != major_num:
                count -= 1
            else:
                count += 1
        return major_num

sol = Solution()
print sol.majorityElement([1,2,3,2,2,1,1,2,2,2,2,1,1,1,1,1,1])
