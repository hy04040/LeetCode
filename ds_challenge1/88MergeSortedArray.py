from typing import List
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums = nums1[0:m]
        p_idx = 0
        q_idx = 0
        for i in range (0,n+m):
            if q_idx == n or (p_idx != m and nums[p_idx] < nums2[q_idx]):
                nums1[i] = nums[p_idx]
                p_idx += 1
            else:
                nums1[i] = nums2[q_idx]
                q_idx += 1
        return nums1

sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
answer = sol.merge(nums1,m,nums2,n)
print(answer)
        