class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        mini = 0
        profit = 0
        for i in range(mini, len(prices)):
            if prices[i] < min:
                min = prices[i]
                mini = i
            if profit < prices[i] - min:
                profit = prices[i] - min
            


        return profit
            
