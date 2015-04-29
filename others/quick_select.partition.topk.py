#partion an array, such that all elements smaller than arr[x] are before those larger than x.
class Solution:
    def qselect(self, A, k):
        if len(A) < k: return A
        pivot = A[-1]
        right = [pivot] + [x for x in A[:-1] if x >= pivot]
        rlen = len(right)
        if rlen == k:
            return right
        if rlen > k:
            return self.qselect(right, k)
        else:
            left = [x for x in A[:-1] if x < pivot]
            return self.qselect(left, k - rlen) + right

sol = Solution()
#top k
for i in xrange(1, 10):
    print sol.qselect([1,8,4,3,10,9,2,7,6,5], i)
