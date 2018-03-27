"""
brute: sort, O(nlogn)
op: O(n)

"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        for i in xrange(n):
            print '---'
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > n or A[i] == A[A[i] -1]:
                    break
                a = i
                b = A[i] - 1
                # put the num to A[num]
                A[a], A[b] = A[b], A[a]
                print A
            #print A, A[i], i + 1

        for i in xrange(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1

sol = Solution()
print sol.firstMissingPositive([0,4,4,2,1,6])
 
