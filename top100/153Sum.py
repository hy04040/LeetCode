class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        if n < 3:
            return ans
        nums.sort()
        i = 0
        while i<n-2 and nums[i]<=0:
            target = -1*nums[i]
            l_idx = i+1
            r_idx = n-1
            while l_idx < r_idx:
                if nums[l_idx] + nums[r_idx] == target:
                    ans.append([nums[i], nums[l_idx], nums[r_idx]])
                    while l_idx<r_idx and nums[l_idx] == nums[l_idx+1]:
                        l_idx += 1
                    l_idx += 1
                    r_idx -= 1
                elif nums[l_idx] + nums[r_idx] < target:
                    l_idx += 1
                else:
                    r_idx -= 1
            while i<n-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans
nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))


class Solution(object):
    def threeSum(self, nums):
        ans = []
        table = {}
        triplet = []
        n = len(nums)
        if n < 3:
            return ans
        nums.sort()
        for i in range(0, n-2):
            if  0<nums[i]:
                break
            if nums[i] in table:
                pass
            else:
                table[nums[i]] = True
                l_idx = i+1
                r_idx = n-1
                target = -1*nums[i]
                while l_idx < r_idx:
                    if nums[l_idx] + nums[r_idx] == target:
                        if {nums[i],nums[l_idx],nums[r_idx]} not in triplet:
                            triplet.append({nums[i],nums[l_idx],nums[r_idx]})
                            ans.append([nums[i], nums[l_idx], nums[r_idx]])
                        r_idx -= 1
                    elif nums[l_idx] + nums[r_idx] < target:
                        l_idx += 1
                    else:
                        r_idx -= 1
        return ans
