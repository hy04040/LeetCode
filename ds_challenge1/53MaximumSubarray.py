from typing import List
##do dp ##
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def cross_max_subarrays(nums,p,q,r):
            l_max = r_max = -1000000000
            t_sum = 0
            for i in range(q+1,r+1):
                t_sum += nums[i]
                if l_max < t_sum:
                    l_max = t_sum
            t_sum = 0
            for i in range(q,p-1,-1):
                t_sum += nums[i]
                if r_max < t_sum:
                    r_max = t_sum
            return l_max + r_max
        def max_subarrays(nums, p,r):
            if p<r:
                q = (p+r)//2
                left = max_subarrays(nums,p,q)
                right = max_subarrays(nums,q+1,r)
                cross = cross_max_subarrays(nums,p,q,r)
                result = max(left,right,cross)
                return result
            return nums[p]
        return max_subarrays(nums,0,len(nums)-1)

sol = Solution()
answer = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(answer)

        