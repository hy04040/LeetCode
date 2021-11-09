from typing import List

class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range (1,numRows+1):
            row = []
            for j in range (0,i):
                if j == 0 or j == i-1:
                    row.append(1)
                else:
                    row.append(triangle[i-2][j-1]+triangle[i-2][j])
            triangle.append(row)
        return triangle
    """
    def generate(self, numRows):
        triangle = []
        for i in range (1,numRows+1):
            row = []
            for j in range (0,i):
                if j == 0 or j == i-1:
                    row.append(1)
                else:
                    row.append(triangle[i-2][j-1]+triangle[i-2][j])
            triangle.append(row)
        return triangle
    """
        



sol = Solution()
answer = sol.generate(5)
print(answer)