from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule = {}
        for i in range(0, len(prerequisites)):
            preq = prerequisites[i]
            if preq[0] in schedule:
                schedule[preq[0]].append(preq[1])
            else:
                schedule[preq[0]] = [preq[1]]
        flag = True
        def dfs(i):
            nonlocal flag
            if i not in schedule:
                return
            visited[i] = 1
            for preq in schedule[i]:
                if visited[preq] == 1:
                    flag = False
                    return
                if visited[preq] == 0:
                    dfs(preq)
                    visited[preq] = 2
        for key in schedule:
            visited = [0 for j in range(numCourses)]
            if visited[key] == 0:
                dfs(key)
                if flag == False:
                    return False
        return True    



numCourses = 2
prerequisites = [[1,0],[0,1]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))

