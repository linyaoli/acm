class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0 or len(A) == 1:
            return len(A)
        i = 0
        j = 1
        while j < len(A):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
            j += 1

        return i + 1

        
