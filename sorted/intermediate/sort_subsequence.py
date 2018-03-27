# sort the shortest subsequence of an array, thus the array is sorted.
# return index
# 1,2,4,7,10,11,7,12,6,7,16,18,19
# return
#

class Solution:
    def findSeq(self, arr):
        l = self.endOfLeft(arr)
        r = self.startOfRight(arr)
        arr_s = sorted(arr[l:r+1])
        #TODO: find merge indices
        #do this later.

    def endOfLeft(self, arr):
        for i in xrange(len(arr)-1):
            if arr[i] > arr[i + 1]:
                return i
        return len(arr) - 1

    def startOfRight(self, arr):
        for i in xrange(len(arr)-1, 0, -1):
            if arr[i] < arr[i - 1]:
                return i
        return 0



sol = Solution()
print sol.findSeq([1,2,4,7,10,11,7,12,6,7,16,18,19])
