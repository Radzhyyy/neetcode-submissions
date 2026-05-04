class Solution:
    def maxProfit(self, prices):
 

        l = 0 

        maX = 0

        for r in range(len(prices)):

            if prices[r] < prices[l]:
                prices[l] = prices[r]

            else:

                profit = prices[r] - prices[l]
                maX = max(maX, profit)


        return maX
