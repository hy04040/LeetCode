class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = [[0 for x in range(n)] for y in range(n)] 
        for i in range(0,n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(0,n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j], dp[i-1][j+1])
        return min(dp[n-1])

        

matrix = [[-19,57],[-40,-5]]
sol = Solution()
print(sol.minFallingPathSum(matrix))