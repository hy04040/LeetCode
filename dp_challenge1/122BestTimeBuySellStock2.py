class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        for i in range(1,n):
            max_profit += max(0, prices[i]-prices[i-1])
        return max_profit





sol = Solution()
prices = [7,1,5,3,6,4]
answer = sol.maxProfit(prices)
print(answer)