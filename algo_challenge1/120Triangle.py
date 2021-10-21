class Solution(object):
    def minimumTotal(self, triangle):
        dp = [[0]*len(i) for i in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(0,len(triangle[i])):
                if j-1 < 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif len(triangle[i-1]) == j:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[len(triangle)-1])



sol = Solution()
answer = sol.minimumTotal([[-10]])
print(answer)