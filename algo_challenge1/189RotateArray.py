from typing import List
import math
class Solution(object):
    def rotate(self, nums, k):
        nums = nums[len(nums)-k:len(nums)] + nums[0:len(nums)-k]
        print(nums)
        

sol = Solution()
answer = sol.rotate([1,2,3,4,5,6,7],3)
print(answer)
        