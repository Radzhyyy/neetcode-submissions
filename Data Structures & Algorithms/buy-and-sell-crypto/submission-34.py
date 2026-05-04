class Solution:
    def maxProfit(self, prices):

        l = 0
        maX = 0

        for r in range(1, len(prices)):

            if prices[r] < prices[l]:
                l = r

            else:
                profit = prices[r] - prices[l]
                maX = max(maX, profit)

        return maX