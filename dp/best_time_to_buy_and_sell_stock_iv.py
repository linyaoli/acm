class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit2(self, k, prices): # allow max k transactions.
        if k > len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        bought = [float('-inf')] * (k + 1) # maximum profit after buying at prices[idx] in transaction i.
        sold = [0] * (k + 1) # maximum profit after selling at prices[idx] in transaction i.

        for price in prices:
            for i in xrange(1, k + 1): # what's the best solution for one transaction?
                sold[i] = max(sold[i], bought[i] + price)
                bought[i] = max(bought[i], sold[i - 1] - price)
                print sold, bought

        return sold[k]

    def maxProfit(self, k, prices):
        hold1 = hold2 = -2**31
        release1 = release2 = 0
        for i in prices:
            release2 = max(release2, hold2 + i) #if we sold at last price, simply buy now.
            hold2 = max(hold2, release1 - i) #if we bought at last price, must sell then buy.
            release1 = max(release1, hold1 + i) # if we sold at current price
            hold1 = max(hold1, -i) # if we bought

        return release2

sol = Solution()
#print sol.maxProfit(1, [2, 1])
#print sol.maxProfit(1, [1, 3])
print sol.maxProfit(4, [1,2,4,2,5,7,2,4,9,0])
