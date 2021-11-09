class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        for i in range(0,m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(0,n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
        
obstacleGrid = [[0,0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid))