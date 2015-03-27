"""
A long array A[] is given to you. There is a sliding window of size w which is
moving from the very left of the array to the very right. You can only see the
w numbers in the window. Each time the sliding window moves rightwards by one
position. Following is an example:

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

this solution's complexity: O(n)

"""


class Solution:
    def getMax(self, arr, w):
        n = len(arr)
        ret = [0] * (n - w + 1)
        queue = []

        for i in xrange(w):
            while queue != [] and arr[i] >= arr[queue[-1]]:
                queue.pop()
            queue.append(i)
        # queue saves the indices, this queue must ensure that the largest
        # number will always be in the front.
        for i in xrange(w, n):
            ret[i - w] = arr[queue[0]]

            while queue != [] and arr[i] >= arr[queue[-1]]:
                # if the newest number is larger than the smallest in last window.
                # remove it.
                queue.pop()
            while queue != [] and queue[0] <= i - w:
                # if the largest number is already out of the window, remove it.
                queue.pop(0)
            # now arr[i] must be the smallest in the queue since all those smaller ones have been removed.
            queue.append(i)

        ret[n - w] = arr[queue[0]]
        return ret

sol = Solution()
print sol.getMax([1,3,-1,-3,5,3,6,7], 3)
