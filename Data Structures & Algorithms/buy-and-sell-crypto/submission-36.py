class Solution:
    def maxProfit(self, prices):
        l = 0

        MAX = 0



        for i in range(1, len(prices)):

            if prices[i] < prices[l]:
                l = i

            else:
                profit = prices[i] - prices[l]
                MAX = max(MAX, profit)


        return MAX