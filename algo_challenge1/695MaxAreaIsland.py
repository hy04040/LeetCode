from typing import List
import math
class Solution(object):
    def maxAreaOfIsland(self, grid):
        def is_inside(i,j,c_len,r_len):
            return -1<i and i<c_len and -1<j and j<r_len
        def bfs(i,j,visited,grid):
            c_len, r_len = len(grid),len(grid[0])
            direction = [[-1,0],[0,-1],[0,1],[1,0]]
            bfs = []
            bfs.append([i,j])
            visited[i][j] = 1
            cnt = 1
            while len(bfs) != 0:
                src = bfs.pop(0)
                for d in direction:
                    x = src[0] + d[0]
                    y = src[1] + d[1]
                    if is_inside(x,y,c_len, r_len) and grid[x][y] == 1 and visited[x][y] == 0:
                        visited[x][y] = 1
                        cnt += 1
                        bfs.append([x,y])
            return cnt
        c_len, r_len = len(grid),len(grid[0])
        visited = [[0 for i in range(r_len)] for j in range(c_len)]
        max_cnt = 0
        for i in range (0,c_len):
            for j in range (0,r_len):
                if grid[i][j]== 1 and visited[i][j] == 0:
                    cnt = bfs(i,j,visited,grid)
                    if max_cnt < cnt:
                        max_cnt = cnt
        return max_cnt        
        
        
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
answer = sol.maxAreaOfIsland(grid)
print(answer)
        