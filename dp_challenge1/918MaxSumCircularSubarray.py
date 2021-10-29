class Solution(object):
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        max_val = total = min_val = nums[0]
        dp_max = [0]*n
        dp_min = [0]*n
        dp_max[0] = dp_min[0] = nums[0]
        if n == 1:
            return nums[0]
        for i in range(1, n):
            total += nums[i]
            if 0 <= dp_max[i-1]:
                dp_max[i] = dp_max[i-1] + nums[i]
            else:
                dp_max[i] = nums[i]
            if dp_min[i-1] < 0:
                dp_min[i] = dp_min[i-1] + nums[i]
            else:
                dp_min[i] = nums[i]
        max_val = max(dp_max)
        min_val = min(dp_min)
        if total - min_val == 0:
            min_val = max(nums)
        return max(max_val, total-min_val)
        


sol = Solution()
nums = [-2]
answer = sol.maxSubarraySumCircular(nums)
print(answer)