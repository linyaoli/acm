class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # Assume we can complete transactions as many as possible.
        # We shall buy stocks every time it is going to rise.
        # i.e.  1 2 3 4 -> 1 - 4 = 1 - 2 + 2 - 3 + 3 - 4
        sum = 0
        length = len(prices)

        for idx in xrange(0, length - 1):
            diff = prices[idx + 1] - prices[idx];
            if diff > 0:
                sum += diff
        return sum
