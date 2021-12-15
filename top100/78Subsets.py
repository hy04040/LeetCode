class Solution(object):
    def subsets(self, nums):
        ans = []
        
        def dfs(idx, res):
            if idx == len(nums):
                ans.append(res[:])
                return
            dfs(idx+1, res[:])
            res.append(nums[idx])
            dfs(idx+1, res[:])
        dfs(0, [])
        return ans
        
        

nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))


class Solution(object):
    def subsets(self, nums):
        ans = []
        
        def dfs(idx, res):
            if idx == len(nums):
                ans.append(res[:])
                return
            res.append(nums[idx])
            dfs(idx+1, res)
            res.pop()
            dfs(idx+1, res)
        dfs(0, [])
        return ans

nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))
        