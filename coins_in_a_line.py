"""
There are n coins in a line. (Assume n is even). Two players take turns to take
a coin from one of the ends of the line until there are no more coins left.
The player with the larger amount of money wins.

1. Would you rather go first or second? Does it matter?
2. Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.

"""
# If go first , we have the advantages of:
# 1. pick the larger one at first.
# 2. if the num is odd, we can pick one more coin.

class Solution:
    def coins(self, arr):
