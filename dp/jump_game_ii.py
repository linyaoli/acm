class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # greedy algorithm.
        start = end = count = 0
        # two pointers to maintain a range
        # each time finds the maximum A[i] + i
        if len(A) == 1: return 0
        while (end < len(A)):
            max_n = 0
            count += 1
            # Among the range which current item can reach,
            # find the futhurest end
            for i in xrange(start, end+1):
                if A[i] + i >= len(A) - 1:
                    return count
                max_n = max(max_n, A[i] + i)
            start = end + 1
            end = max_n
