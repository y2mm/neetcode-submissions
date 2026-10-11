class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min = prices[0]
        # min = 0
        # max = 0
        # maxi = 0
        profit = 0
        for i, val in enumerate(prices):
            for j in range(i+1, len(prices)):
                if (prices[j]-prices[i]) > profit:
                    profit = prices[j]-prices[i]


        return profit
            
