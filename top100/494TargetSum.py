class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}
        def dfs(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            if (idx, total) in dp:
                return dp[(idx, total)]
            dp[(idx, total)] = (dfs(idx+1, total+nums[idx]) + dfs(idx+1, total-nums[idx]))
            return dp[(idx, total)]
        dfs(0, 0)
        return dp[(0,0)]
        
        

nums = [1,1,1,1,1]
target = 3
nums = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
target = 35
nums = [1,1,1,1,1]
target = 3
sol = Solution()
print(sol.findTargetSumWays(nums, target))

class Solution(object):
    def findTargetSumWays(self, nums, target):
        cnt = total =0
        def dfs(idx, total):
            nonlocal cnt
            if idx == len(nums):
                if total == target:
                    cnt += 1
                return
            dfs(idx+1, total+nums[idx])
            dfs(idx+1, total-nums[idx])
        dfs(0, 0)
        return cnt
