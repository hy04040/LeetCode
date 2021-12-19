
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = {}
        def helper(r,c):
            if r > m-1 or c > n-1:
                return 0
            if (r,c) not in cache:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diag = helper(r+1, c+1)
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diag)
            return cache[(r,c)]
        helper(0,0)
        max_length = max(cache.values())
        return max_length**2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol = Solution()
print(sol.maximalSquare(matrix))

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        maxSquare = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                square = 0
                if matrix[i][j] == "1":
                    if i+1 < m and j+1 < n:
                        square = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    dp[i][j] = square+1
                    maxSquare = max(maxSquare, dp[i][j])

        return maxSquare*maxSquare