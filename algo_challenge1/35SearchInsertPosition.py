from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_examin(nums, target, p, r):
            if p<r:
                q = (p+r)//2
                if nums[q] == target:
                    return q
                elif nums[q] > target:
                    return binary_examin(nums,target,p,q)
                else:
                    return binary_examin(nums,target,q+1,r)
            if nums[p] <target:
                return p+1
            else:
                return p
        idx = binary_examin(nums,target,0,len(nums)-1)
        return idx
        
sol = Solution()
answer = sol.searchInsert([1],0)
print(answer)