from typing import List
import math
class Solution(object):
    def sortedSquares(self, nums):
        i = 0
        k = j = len(nums)-1
        output = [0]*len(nums)
        while i<=j:
            if abs(nums[i]) < abs(nums[j]):
                output[k] = nums[j]*nums[j]
                j -= 1
                k -= 1
            else:
                output[k] = nums[i]*nums[i]
                i += 1
                k -= 1
        return output
        

sol = Solution()
answer = sol.sortedSquares([-7,-3,2,3,11])
print(answer)
        