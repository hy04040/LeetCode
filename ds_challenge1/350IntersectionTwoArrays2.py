from typing import List
class Solution:
    def intersect(self, nums1, nums2):
        dictionary = {}
        ans = []
        for i in nums1:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        for j in nums2:
            if j in dictionary:
                if dictionary[j] > 0:
                    ans.append(j)
                    dictionary[j] -= 1
        return ans

nums1 = [1,2,2,1]
nums2 = [2,2]
sol = Solution()
answer = sol.intersect(nums1, nums2)
print(answer)