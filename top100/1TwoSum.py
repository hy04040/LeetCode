class Solution(object):
    def twoSum(self, nums, target):
        table = {}
        for i in range(0,len(nums)):
            if (target - nums[i]) in table:
                return [i, table[target - nums[i]]]
            else:
                table[nums[i]] = i
        
        
        
nums = [3,2,4]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))