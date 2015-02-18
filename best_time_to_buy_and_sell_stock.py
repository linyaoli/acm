class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == []:
            return 0
        max_diff = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_diff = max(max_diff, price - min_price)
        return max_diff
            
