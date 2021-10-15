from typing import List

#direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

class Solution(object):
    def isValidSudoku(self, board):
        def validate(board,i,j):
            x,y = i,j
            char = board[i][j]
            #check row
            for row in range(0,9):
                if y != row and board[x][row] == char:
                    return False
            #check col
            for col in range(0,9):
                if x != col and board[col][y] == char:
                    return False
            #check box
            box_x = i - i%3
            box_y = j - j%3
            for row in range (box_x, box_x+3):
                for col in range (box_y, box_y+3):
                    if board[row][col] == char and (row!=i and col!=j):
                        return False
            return True
        ans = True
        for i in range (0,9):
            for j in range (0,9):
                if board[i][j] != ".":
                    if not validate(board,i,j):
                        ans = False
                        return ans
        return ans

        
        


board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
sol = Solution()
answer = sol.isValidSudoku(board)
print(answer)