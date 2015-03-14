class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num) - 1
        ans = num[0]
        while start < end and num[start] >= num[end]:
            mid = start + (end - start) / 2
            if num[mid] > num[end]:
                start = mid + 1
            elif num[mid] < num[start]:
                end = mid
            else:
                start += 1


        return num[start]


sol = Solution()
a=[1,2,3,5,0]
b=[3,5,0,1,2]
c=[5,0,1,2,3]
d=[5,5,5,5,5,5,0,1,1,1,1,1,2]
e = [3,3,1,3]
print sol.findMin(e)
