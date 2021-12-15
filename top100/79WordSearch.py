class Solution(object):
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = [[False]*n for i in range(m)]
        def isSafe(x, y):
            return 0<=x and x<m and 0<=y and y<n
        
        def dfs(idx, x, y):
            if idx == len(word):
                return True
            for d in direction:
                new_x = x + d[0]
                new_y = y + d[1]
                if isSafe(new_x,new_y) and not visited[new_x][new_y] and board[new_x][new_y] == word[idx]:
                    visited[new_x][new_y] = True
                    if dfs(idx+1, new_x, new_y):
                        return True
                    visited[new_x][new_y] = False

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(1, i, j):
                        return True
                    visited[i][j] = False
        return False
        
        
        
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
sol = Solution()
print(sol.exist(board, word))
