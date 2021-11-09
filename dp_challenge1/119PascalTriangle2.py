class Solution(object):
    def getRow(self, rowIndex):
        triangle = [[0 for x in range(rowIndex+1)] for y in range(rowIndex+1)] 
        triangle[0][0] = 1
        for i in range(1, rowIndex+1):
            for j in range(0,i+1):
                if j == 0:
                    triangle[i][j] = triangle[i-1][j]
                elif j == i:
                    triangle[i][j] = triangle[i-1][j-1]
                else:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[rowIndex]


        

rowIndex = 3
sol = Solution()
print(sol.getRow(rowIndex))