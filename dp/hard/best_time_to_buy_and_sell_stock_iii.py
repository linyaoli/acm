class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        k = 2
        if k > len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        bought = [float('-inf')] * (k + 1) # maximum profit after buying at prices[idx] in transaction i.
        sold = [0] * (k + 1) # maximum profit after selling at prices[idx] in transaction i.

        for price in prices:
            for i in xrange(1, k + 1): # what's the best solution for one transaction?
                sold[i] = max(sold[i], bought[i] + price)
                bought[i] = max(bought[i], sold[i - 1] - price)

        return sold[k]
        
