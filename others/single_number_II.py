class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        n = len(A)
        ones = 0
        twos = 0
        for i in xrange(n):
            # ones: binary which appears once
            # twos: binary which appears twice
            # if appears three times, in twos the binary is set to 0.
            # ones ^ A[i] : appears odd times
            _ones = (ones ^ A[i]) & ~twos # those already appear once, those appear twice are set to 0 in _ones.
            # ones & A[i] : A[i] appears once in ones -> now we have twice
            # ~A[i] & twos: A[i] didnt appear in twos -> now the twos remain
            twos = (ones & A[i]) | (~A[i] & twos)
            ones = _ones

        return ones

sol = Solution()
A = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
B = [-2, -2, -2, 3, 3, 3, 1]
C = [7,7,8,8,9,8,7]
print sol.singleNumber(B)
