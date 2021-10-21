class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [-1]*1005
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        return min(dp[len(cost)-2], dp[len(cost)-1])
        
sol = Solution()
answer = sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(answer)