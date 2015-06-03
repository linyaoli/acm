class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        cur = 0
        for idx in xrange(len(A)):
            if A[idx] != elem:
                A[cur] = A[idx]
                cur += 1
        print A
        return cur

sol = Solution()
print sol.removeElement([1,2,3,2,4,3,2], 2)
