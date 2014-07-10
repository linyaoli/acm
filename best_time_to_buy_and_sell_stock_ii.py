class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        sum = 0
        length = len(prices)

        for idx in xrange(0, length - 1):
            diff = prices[idx + 1] - prices[idx];
            if diff > 0:
                sum += diff
        return sum

        
