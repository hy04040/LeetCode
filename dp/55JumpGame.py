from typing import List

class Solution(object):
    def canJump(self, nums):
        reachable = [False]*len(nums)
        last_idx = len(nums) -1
        reachable[0] = True
        for i in range(0, len(nums)):
            if reachable[i]:
                if last_idx <= i + nums[i]:
                    return True
                for idx in range(1,nums[i]+1):
                    reachable[i+idx] = True
        return False

        
        

        
sol = Solution()
answer = sol.canJump([0])
print(answer)

