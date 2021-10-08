from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(a) == len(nums):
            return True
        return False

sol = Solution()
answer = sol.containsDuplicate([1,2,3,1])
print(answer)