class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_profit = prices[0]
        for i in range(1,len(prices)):
            min_profit = min(min_profit, prices[i])
            max_profit = max(max_profit, prices[i]-min_profit)
        return max_profit


prices = [7,1,5,3,6,4]
sol = Solution()
answer = sol.maxProfit(prices)
print(answer)