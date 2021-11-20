class Solution(object):
    def maxArea(self, height):
        n = len(height)
        most_water = 0
        i = 0
        j = n-1
        while i < j:
            water = (j-i)*min(height[i],height[j])
            if most_water < water:
                most_water = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return most_water

        
        
height = [1,2,1]
sol = Solution()
print(sol.maxArea(height))

