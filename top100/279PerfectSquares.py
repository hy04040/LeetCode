from typing import List
from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [ 0 for i in range (n+1)]
        for i in range(1, n+1):
            dp[i] = i
            for k in range(1, isqrt(i)+1):
                dp[i] = min(dp[i], dp[i-k*k]+1)
        return dp[n]

n = 7168
sol = Solution()
print(sol.numSquares(n))

class Solution:
    def numSquares(self, n: int) -> int:
        m = 1
        dp = {}
        squares = []
        dp[0] = 0
        while True:
            square = m**2
            if square < n+1:
                squares.append(square)
                dp[square] = 1
                m += 1
            else:
                break
        for i in range(0, n+1):
            dp[i] = i
            for k in squares:
                if k <= i:
                    dp[i] = min(dp[i], dp[i-k]+1)
        return dp[n]
