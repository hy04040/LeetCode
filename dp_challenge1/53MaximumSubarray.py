class Solution(object):
    def maxSubArray(self, nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if 0 <= dp[i-1]:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


sol = Solution()
nums = [5,4,-1,7,8]
answer = sol.maxSubArray(nums)
print(answer)