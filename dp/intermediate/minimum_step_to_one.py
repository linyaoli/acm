"""
Problem Statement:
On a positive integer, you can perform any one of the following 3 steps.
1.) Subtract 1 from it. ( n = n - 1 )  ,
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  ,
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).
Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

"""
class Solution:
    #F(n) =   1 + min{  F(n-1) ,  F(n/2)  ,  F(n/3)}
    def minStep(self, n):
        #n = len(num)
        m = [0] * (n+1)
        if n == 1: return 0
        if m[-1] == -1: return m[-1]
        for i in xrange(2, n+1):
            #use substract by default.
            m[i] = m[i-1] + 1
            if i % 2 == 0:
                m[i] = min(m[i], 1+m[i/2])
            if i % 3 == 0:
                m[i] = min(m[i], 1+m[i/3])

        return m[-1]

sol = Solution()
print sol.minStep(123)
