"""
6 8 7 4 3 2
1. from right to left, find the first element which violates the increasing order, marked as N.
2. from right to left, find the first element which is larger that N, marked as M.
3. swap N and M.
> 7 8 6 4 3 2
4. reverse all digits on the right of M.
> 7 2 3 4 6 8


""" 
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1:
            return num

        # from right to left, find the first num which violates the increasing trend.
        idx = len(num) - 1
        while idx > 0:
            if num[idx - 1] < num[idx]:
                break
            idx -= 1

        # ..., find the 1st num which is larger than num[idx]
        pn = len(num) - 1
        if idx > 0:
            idx -= 1
            while pn >= 0 and num[pn] <= num[idx]:
                pn -= 1
        # swap idx and pn
            num[idx], num[pn] = num[pn], num[idx]
            idx += 1
        # reverse all digits on the right of idx .
        r_num = num[idx:]
        r_num.reverse()
        return num[:idx] + r_num

sol = Solution()
print sol.nextPermutation([1,3,2])
