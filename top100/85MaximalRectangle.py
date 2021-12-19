from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = maxA = 0
        for i in range(0, n):
            histrogram = []
            for j in range(0, m):
                if matrix[i][j] == "0":
                    histrogram.append(0)
                else:
                    height = 0
                    for h in range(i, -1, -1):
                        if matrix[h][j] == "0":
                            break
                        height += 1
                    histrogram.append(height)
            ## dp on histrogram
            sidx = 0
            S = []
            for i, h in enumerate(histrogram):
                sidx = i
                while S and h<S[-1][1]:
                    idx, height = S.pop(-1)
                    maxA = max(maxA, height*(i-idx))
                    sidx = idx
                S.append((sidx,h))
            for i in range(len(S)):
                idx, height = S[i]
                maxA = max(maxA, height*(len(histrogram)-idx))
        return maxA



              

        

matrix = [["1"]]
sol = Solution()
print(sol.maximalRectangle(matrix))

