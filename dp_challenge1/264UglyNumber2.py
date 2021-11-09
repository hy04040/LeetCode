class Solution(object):
    def nthUglyNumber(self, n):
        dp = [1]*(n+1)
        two = three = five = 1
        for i in range(2,n+1):
            min_num = min(dp[two]*2,dp[three]*3,dp[five]*5)
            dp[i] = min_num
            if min_num == dp[two]*2:
                two += 1
            if min_num == dp[three]*3:
                three += 1
            if min_num == dp[five]*5:
                five += 1
        return dp[n]

        


        

n = 10
sol = Solution()
print(sol.nthUglyNumber(n))