class Solution(object):
    def rob(self, nums):
        dp = [[nums[0]],[0]]
        for i in range(1,len(nums)):
            if i == 1:
                dp[0].append(nums[0])
                dp[1].append(nums[1])
            elif i == len(nums)-1:
                dp[0].append(dp[0][i-1])
                dp[1].append(max(dp[1][i-2]+nums[i],dp[1][i-1]))
            else:
                dp[0].append(max(dp[0][i-2]+nums[i],dp[0][i-1]))
                dp[1].append(max(dp[1][i-2]+nums[i],dp[1][i-1]))
        return max(dp[0][len(nums)-1],dp[1][len(nums)-1])

        
        

sol = Solution()
answer = sol.rob([1,2,3,4,5,1,2,3,4,5])
print(answer)