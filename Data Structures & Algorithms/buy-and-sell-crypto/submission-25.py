class Solution:
    def maxProfit(self, prices):

        MAX = 0 

        l = 0 

        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                MAX = max(MAX, profit)

            else:
                l = r

            r += 1

        return MAX