class Solution:
    def maxProfit(self, prices):

        l = 0

        MAX = 0


        for r in range(1, len(prices)):

            if prices[r] < prices[l]:
                l = r

            else:
                total = prices[r] - prices[l]
                MAX = max(MAX, total)

        return MAX

    