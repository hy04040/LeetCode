class Solution(object):
    def maxScoreSightseeingPair(self, values):
        n = len(values)
        max_score = values[0] + values[1] -1
        dp = [0]*n
        i = 0
        dp[0] = values[0]-1
        for i in range(1, n):
            if max_score < dp[i-1] + values[i]:
                max_score = dp[i-1] + values[i]
            dp[i] = max(dp[i-1]-1, values[i]-1)
        return max_score
        
        


sol = Solution()
values = [5,1,2,2,4,5,3]
answer = sol.maxScoreSightseeingPair(values)
print(answer)