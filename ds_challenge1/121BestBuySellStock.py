from typing import List

## dp ##
class Solution:
    def maxProfit(self, prices):
        min_profit = prices[0]
        max_profit = 0
        for i in range (1,len(prices)):
            min_profit = min(min_profit,prices[i])
            max_profit = max(max_profit, prices[i]-min_profit)
        return max_profit

sol = Solution()
answer = sol.maxProfit([7,6,4,3,1])
print(answer)