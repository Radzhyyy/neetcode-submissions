class Solution:
    def maxProfit(self, prices):

        l = 0 # buy 

        r = 1 # sell

        p = 0 # profit 

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                p = max(p, profit)


            else:
                l = r
            r += 1

        return p