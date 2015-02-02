class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        max_cover = 0
        for i in xrange(len(A)):
            max_cover = max(max_cover - 1, A[i])
            if max_cover == 0 and i < len(A) - 1:
                return False

        return True

sol = Solution()
print sol.canJump([3,2,1,0,4])
