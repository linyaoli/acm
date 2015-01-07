class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        cur = 0
        for idx in xrange(0, length, 1):
            if A[idx] == elem:
                continue
            A[cur] = A[idx]
            cur += 1
        return cur
