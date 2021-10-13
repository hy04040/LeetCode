from typing import List

class Solution:
    def matrixReshape(self, mat, r, c):
        linear = [0]*(r+c)
        output = [[0]*c for _ in range(r)]
        mat_r = len(mat)
        mat_c = len(mat[0])
        if mat_r*mat_c != r*c:
            return mat
        r_idx = c_idx = 0
        for i in range (0, r*c):
            r_idx = i // c
            c_idx = i % c
            mr_idx = i // mat_c
            mc_idx = i % mat_c
            output[r_idx][c_idx] = mat[mr_idx][mc_idx]
        """
        for i in range (0,len(mat)):
            for j in range (0, len(mat[0])):
                output[r_idx][c_idx] = mat[i][j]
                c_idx += 1
                if c_idx == c:
                    r_idx += 1
                    c_idx = 0
        """
        return output



sol = Solution()
answer = sol.matrixReshape([[1,2],[3,4]],1,4)
print(answer)