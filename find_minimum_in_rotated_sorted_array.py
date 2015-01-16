class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num) - 1
        ans = num[0]
        while start <= end:
            mid = start + (end - start) / 2
            if num[mid] <= num[end]:
                end = mid - 1
            else:
                start = mid + 1
            ans = min(ans, num[mid])
        return ans


sol = Solution()
a=[1,2,3,5,0]
b=[3,5,0,1,2]
c=[5,0,1,2,3]
d=[3,4,5,0,2]
e = [1]
print sol.findMin(e)
