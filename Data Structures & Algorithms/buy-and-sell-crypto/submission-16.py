class Solution:
    def maxProfit(self, prices):
        l = 0
        r = 1
        MAX = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                MAX = max(MAX, profit)

            else:
                l = r

            r += 1

        return MAX