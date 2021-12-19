from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        S = []
        maxA = sidx = 0
        for i in range(0, len(heights)):
            sidx = i
            while S and heights[i] < S[-1][1]:
                (idx, height) = S.pop(-1)
                maxA = max(maxA, (i-idx)*height)
                sidx = idx
            S.append((sidx,heights[i]))
        while S:
            (idx, height) = S.pop()
            maxA = max(maxA, (len(heights)-idx)*height)
        return maxA


              

        

heights = [2,1,5,6,2,3]
sol = Solution()
print(sol.largestRectangleArea(heights))


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = h = 0
        for i in range(0, len(heights)):
            if h != heights[i]:
                h = heights[i]
                ridx = lidx = i
                for idx in range (i, -1, -1):
                    if heights[idx] < h:
                        break
                    ridx = idx
                for idx in range (i, len(heights)):
                    if heights[idx] < h:
                        break
                    lidx = idx
                ans = max(ans, h*(lidx-ridx+1))
        return ans
