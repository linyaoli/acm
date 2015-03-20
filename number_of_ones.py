class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            n &= n-1
            cnt += 1
        return cnt
        
