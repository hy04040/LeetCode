from typing import List
import math
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        def is_inside(i,j,c_len,r_len):
            if -1<i and i<c_len and -1<j and j<r_len:
                return True
            return False
        direction = [[-1,0],[0,-1],[0,1],[1,0]]
        c_len,r_len = len(image),len(image[0])
        visited = [[0 for i in range(r_len)] for j in range(c_len)]
        bfs = [[sr,sc]]
        visited[sr][sc] = 1
        color = image[sr][sc]
        image[sr][sc] = newColor
        while len(bfs) != 0:
            src = bfs.pop(0)
            for d in direction:
                x = src[0] + d[0]
                y = src[1] + d[1]
                if is_inside(x,y,c_len,r_len) and image[x][y]==color and visited[x][y] == 0:
                    image[x][y] = newColor
                    visited[x][y] = 1
                    bfs.append([x,y])

        return image
        
        
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0 
newColor = 2
sol = Solution()
answer = sol.floodFill(image,sr,sc,newColor)
print(answer)
        