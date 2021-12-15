class Solution(object):
    def permute(self, nums):
        ans = []

        if len(nums) == 1:
            return [nums[:]]
        for i in range(0, len(nums)):
            n = nums.pop(0)
            per = self.permute(nums)
            for p in per:
                p.append(n)
            ans += per
            nums.append(n)

        return ans
        
        

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))

class Solution(object):
    def permute(self, nums):
        ans = []

        if len(nums) == 1:
            return [nums[:]]
        for i in range(0, len(nums)):
            n = nums.pop(0)
            per = self.permute(nums)
            for p in per:
                p.append(n)
            ans += per
            nums.append(n)

        return ans