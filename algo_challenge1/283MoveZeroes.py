from typing import List
import math
##do this again using quick sort##
class Solution(object):
    def moveZeroes(self, nums):
        nums_length = len(nums)
        output = [-1]*nums_length
        j = nums_length
        k = 0
        for i in range (0,nums_length):
            if nums[i] == 0:
                j -= 1
            else:
                nums[k] = nums[i]
                k += 1
        nums[j:] = [0]*(nums_length-j)
        return nums
        

sol = Solution()
answer = sol.moveZeroes([0])
print(answer)
        