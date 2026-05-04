class Solution:
    def maxProfit(self, prices):
        l = 0


        MAX = 0


        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]
            MAX = max(MAX, profit)


        return MAX