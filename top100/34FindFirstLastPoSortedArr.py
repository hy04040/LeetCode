class Solution(object):
    def searchRange(self, nums, target):
        start = end = -1
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                start = mid
                r = mid -1
            elif nums[mid] < target:
                if mid != len(nums)-1 and nums[mid+1] == target:
                    start = mid+1
                    break
                else:
                    l = mid + 1
            else:
                r = mid - 1
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                end = max(end, mid)
                l = mid + 1
            elif nums[mid] > target:
                if mid != 0 and nums[mid-1] == target:
                    end = mid-1
                    break
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return [start, end]
        

        

nums = [5,7,7,6,8,8,10]
target = 6
sol = Solution()
print(sol.searchRange(nums, target))

