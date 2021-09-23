from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumped = idx = cur_idx = 0;
        for i in range(0,len(nums)):
            idx = max(idx, i+nums[i])
            if i == cur_idx:
                cur_idx = idx;
                jumped += 1
        return jumped
        
sol = Solution()
fp = open("input.txt", "r")
string = fp.readlines()
nums = list(map(int, string[0].split(",")))
answer = sol.jump(nums)
print(answer)