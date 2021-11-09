class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        num_slices = diff = 0
        n = len(nums)
        if len(nums) < 3:
            return 0
        diff = nums[1] - nums[0]
        dp = [0]*n
        for i in range(2, n):
            if diff == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
                diff = nums[i] - nums[i-1]
        return sum(dp)


        

nums = [1,2,3,4,8,9,10]
nums = [2,1,3,4,2,3]
sol = Solution()
print(sol.numberOfArithmeticSlices(nums))