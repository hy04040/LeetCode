class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return nums
        for idx, val in reversed(list(enumerate(nums))):
            if idx == 0:
                nums.sort()
            else:
                if nums[idx-1] < nums[idx]:
                    bigger = idx
                    for i,v in enumerate(nums[idx:]):
                        if nums[idx-1] < v:
                            bigger = i+idx
                        else:
                            break
                    nums[idx-1], nums[bigger] = nums[bigger], nums[idx-1]
                    temp = nums[idx:]
                    temp.sort()
                    nums[idx:] = temp
                    break
        return nums


        
nums = [4, 6, 5, 1]
sol = Solution()
print(sol.nextPermutation(nums))