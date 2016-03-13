"""
https://www.hackerrank.com/challenges/stockma
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
#### read the count of numbers
for i in xrange(t):
  n = int(raw_input())
  profit = 0
  arr = raw_input().split()
                  for j in xrange(n):
                    arr[j] = int(arr[j])
                                ## calculate max profit
                                    ## DP : save the max price after one day.
                                        dp = [0] * n
                                            dp[-1] = arr[-1]
                                                for j in xrange(n-2, -1, -1):
                                                  dp[j] = max(dp[j+1], arr[j])
                                                                  for j in xrange(n):
                                                                    profit += max(0, dp[j] - arr[j])
                                                                                        print profit
