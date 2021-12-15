class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        ans = []
        def dfs(idx, curr, total):
            if total == target:
                ans.append(curr[:])
                return
            if total > target or idx >= len(candidates):
                return
            curr.append(candidates[idx])
            dfs(idx, curr, total+ candidates[idx])
            curr.pop()
            dfs(idx+1, curr, total)
        dfs(0, [], 0)
        return ans        

        

candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))

