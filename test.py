class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        flag0 = 0
        flag2 = len(A) - 1
        flag1 = 0
        while flag1 <= flag2:
            if A[flag1] == 2:
                A[flag1], A[flag2] = A[flag2], A[flag1]
                flag2 -= 1
            elif A[flag1] == 0:
                A[flag0], A[flag1] = A[flag1], A[flag0]
                flag0 += 1
                flag1 += 1
            else:
                flag1 += 1

        return A



sol = Solution()
print sol.sortColors([0, 2,1])
