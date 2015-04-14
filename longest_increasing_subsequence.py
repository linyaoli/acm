"""
Let arr[0..n-1] be the input array and L(i) be the length of the LIS till index i such that arr[i]
is part of LIS and arr[i] is the last element in LIS, then L(i) can be recursively written as.
L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
To get LIS of a given array, we need to return max(L(i)) where 0 < i < n
So the LIS problem has optimal substructure property as the main problem can be solved using solutions to subproblems.

"""

class Solution:
    def LIS(self, num):
        #O(n^2)
        n = len(num)
        lis = [1] * n

        for i in xrange(1, n):
            for j in xrange(i):
                #if num[i] > num[j] that means num[i] is
                #in the subsequence of num[j].
                if num[i] > num[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)

    def naive(self, num, n, max_ref):
        #a naive recursive solution, O(2^n)
        if n == 1:  return 1
        ans = max_end = 1
        #recursively get all LIS ending with num.
        for i in xrange(1, n):
            ans = self.naive(num, i, max_ref)
            if num[i-1] < num[n-1] and ans + 1 > max_end:
                max_end = ans + 1
        if max_ref < max_end:
            max_ref = max_end

        return max_end


sol = Solution()
print sol.naive([10, 22, 9, 33, 21, 50, 41, 60], 8, 1)
print sol.LIS([10, 22, 9, 33, 21, 50, 41, 60])
