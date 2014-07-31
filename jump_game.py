class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        """
         jump[i] = max(jump[i-1], A[i-1]) -1, i!=0
         = 0 , i==0
        """
        n = len(A)
        maxCover = 0
        start = 0
        while start <= maxCover and start < n:
            if A[start] + start > maxCover:
                maxCover = A[start] + start
            if maxCover >= n - 1:
                return True
            start += 1

        return False
        
