"""
9/13/2024
Back Forward Maximizing
"""

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        while prices and prices[-1] == 0: prices.pop()

        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit = max(profit, prices[i] - buy)      
            else:
                buy = prices[i]
        return profit


"""
#Old attempt that took about a hour
class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 0
        profit = 0
        while prices and prices[-1] == 0: prices.pop()

        for i in range(len(prices)):
            if prices[i] <= prices[buy]:
                buy = i

                if sell <= buy:
                    sell = buy
                    for j in range(buy, len(prices)):
                        if prices[j] >= prices[sell]:
                            sell = j
                profit = max(profit, prices[sell] - prices[buy])      

        return profit
"""
