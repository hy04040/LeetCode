class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        dp = [0]*n
        max_val = nums[0]
        dp[0] = curr = nums[0]
        for i in range(1, n):
            if nums[i] == 0:
                dp[i] = 0
                curr = 0
            else:
                dp[i] = min(dp[i-1]*nums[i], curr*nums[i], nums[i])
                curr = max(dp[i-1]*nums[i], curr*nums[i], nums[i])
            if max_val < curr:
                max_val = curr
        return max_val




        


sol = Solution()
nums = [5,5,0,2,6]
answer = sol.maxProduct(nums)
print(answer)