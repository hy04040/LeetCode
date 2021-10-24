from typing import List

class Solution(object):
    def jump(self, nums):
        dp = [-1]*len(nums)
        dp[0] = 0
        curr_idx = jump = 0
        if len(nums) == 1:
            return 0
        for i in range(0,len(nums)):
            for j in range(1,nums[i]+1):
                if len(nums)-1 <= i+j:
                    return dp[i]+1
                if dp[i+j] == -1:
                    dp[i+j] = dp[i] + 1



sol = Solution()
nums = [1]
answer = sol.jump(nums)
print(answer)
 