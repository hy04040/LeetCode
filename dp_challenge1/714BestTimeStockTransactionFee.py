class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n == 1:
            return 0
        dp = [ [0]*2 for i in range(n)]
        dp[0][0] = 0 # no stock
        dp[0][1] = -prices[0] # have stock
        dp[1][0] = max(dp[0][1] + prices[1]-fee, dp[0][0])
        dp[1][1] = max(dp[0][0] - prices[1], dp[0][1])
        max_profit = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1]+prices[i]-fee, dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        print(dp)
        return max(dp[n-1][0],dp[n-1][1])
            


sol = Solution()
prices = [1,3,2,8,4,9]
fee = 2
answer = sol.maxProfit(prices, fee)
print(answer)