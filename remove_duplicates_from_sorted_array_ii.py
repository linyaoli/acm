# duplicates will only allow appear once. 
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0 or len(A) == 1:
            return len(A)
        i = 0
        count = 1
        for j in xrange(1, len(A)):
            if A[i] != A[j]:
                count = 1
                i += 1
                A[i] = A[j]
            else:
                if count < 2:
                    i += 1
                    A[i] = A[j]
                    count += 1
        return i+1
