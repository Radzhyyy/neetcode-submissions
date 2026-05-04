class Solution:
    def maxProfit(self, prices):
        l = 0 # buy day
        r = 1 # sell day
        Max = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                Max = max(Max, profit)

            else:
                l = r
            r += 1

        return Max