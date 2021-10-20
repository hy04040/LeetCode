class Solution(object):
    def climbStairs(self, n):
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range (2,n):
            dp.append(dp[i-1]+ dp[i-2])
        return dp[n-1]
        
sol = Solution()
answer = sol.climbStairs(3)
print(answer)