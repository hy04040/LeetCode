class Solution(object):
    def search(self, nums, target):
        l,r = 0, len(nums)-1
        while l <= r:
            q = (l+r) // 2
            if nums[q] == target:
                return q
            if nums[l] <= nums[q]:
                if nums[l] <= target <= nums[q]:
                    r = q-1
                else:
                    l = q+1
            else:
                if nums[q] <= target <= nums[r]:
                    l = q+1
                else:
                    r = q-1
        return -1
        

        

nums = [4,5,6,7,0,1,2]
target = 3
sol = Solution()
print(sol.search(nums, target))


class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        min_num = min(nums)
        pivot = nums.index(min_num)
        def binary_search(nums, p, r, target):
            while p <= r:
                q = (p+r) //2
                if nums[q] == target:
                    return q
                elif target < nums[q]:
                    return binary_search(nums, p, q-1, target)
                else:
                    return binary_search(nums, q+1, r, target)
        result1 = binary_search(nums, 0, max(pivot-1, 0), target)
        result2 = binary_search(nums,  pivot, max(n-1, 0), target)
        if result1 is not None:
            return result1
        elif result2 is not None:
            return result2
        else:
            return -1
