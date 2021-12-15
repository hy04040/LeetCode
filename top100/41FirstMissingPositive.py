class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        table = {}
        for i in range(1, n+1):
            table[i] = False
        for i in nums:
            if i in table:
                table[i] = True
        for key in table:
            if table[key] == False:
                return key
        return n+1
              

        

nums = [2, 1]
sol = Solution()
print(sol.firstMissingPositive(nums))

