from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, p, r):
            if p<r:
                q = (p+r)//2
                if nums[q] == target:
                    return q
                if target < nums[q]:
                    return binary_search(nums,target,p,q)
                else:
                    return binary_search(nums,target,q+1,r)
            return -1
        nums.sort()
        result = binary_search(nums,target, 0, len(nums))
        return result


sol = Solution()
answer = sol.search([-1,0,3,5,9,12],2)
print(answer)