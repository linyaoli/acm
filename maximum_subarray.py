class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = 0
        max = -100000
        for item in A:
            sum += item
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max
