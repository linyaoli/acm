class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num) - 1
        while start < end:
            mid = start + (end - start) / 2
            if num[start] <= num[mid] and num[mid] <= num[end]:
                pass
            else:
                if (start + 1 == mid or start == mid) and (end == mid or mid + 1 == end):
                    return min(num[start], num[mid], num[end])

            if num[mid] > num[end]: #minimum has to be between mid and end
                start = mid
            if num[mid] < num[end]: # minimum has to be between mid and start
                end = mid
        return num[start]



sol = Solution()
a=[1,2,3,5,0]
b=[3,5,0,1,2]
c=[5,0,1,2,3]
d=[3,4,5,0,2]
e = [1]
print sol.findMin(e)
