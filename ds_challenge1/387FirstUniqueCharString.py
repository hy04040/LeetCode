from typing import List

class Solution(object):
    def firstUniqChar(self, s):
        dictionary = {}
        for c in s:
            if c not in dictionary:
                dictionary[c] = 1
            else:
                dictionary[c] += 1
        for idx,val in enumerate(s):
            if dictionary[val] == 1:
                return idx
        return -1

        
        
    

s =  "aabb"
sol = Solution()
answer = sol.firstUniqChar(s)
print(answer)