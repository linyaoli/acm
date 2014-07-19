class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == []:
            return 0
        max_diff = 0
        min_price = prices[0]
        for price in prices:
            if min_price > price:
                min_price = price
            if price - min_price > max_diff:
                max_diff = price - min_price
        return max_diff
            
