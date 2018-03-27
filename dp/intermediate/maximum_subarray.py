"""
Max[i+1] = Max[i] + A[i+1],  if (Max[i] + A[i+1] >0)
                = 0, if(Max[i]+A[i+1] <0) -> means A[i+1] gotta be negative.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = 0
        max = -2**31
        for item in A:
            sum += item
            if sum > max: max = sum
            if sum < 0: sum = 0
        return max
