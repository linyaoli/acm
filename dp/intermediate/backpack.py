"""
Given n items with size A[i], an integer m denotes the size of a backpack.
How full you can fill this backpack?

Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can
select 2, 3 and 5, so that the max size we can fill this backpack is 10.
If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

"""
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [False] * (m + 1)
        dp[0] = True
        for i in xrange(1, n+1):
            for j in xrange(m, -1, -1):
                if j - A[i-1] >= 0 and dp[j - A[i-1]]:
                    dp[j] = dp[j - A[i-1]]

        for i in xrange(m, -1, -1):
            if dp[i] : return i


sol = Solution()
print sol.backPack(10, [3,4,8,5])
