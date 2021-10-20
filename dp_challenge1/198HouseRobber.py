class Solution(object):
    def rob(self, nums):
        dp = []
        dp.append(nums[0])
        for i in range(1,len(nums)):
            if i == 1:
                dp.append(max(nums[0], nums[1]))
            else:
                dp.append(max(dp[i-2]+nums[i], dp[i-1]))
        return dp[len(nums)-1]
        

sol = Solution()
answer = sol.rob([2,7,9,3,1])
print(answer)