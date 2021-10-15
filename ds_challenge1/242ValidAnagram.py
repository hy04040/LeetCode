from typing import List

class Solution(object):
    def isAnagram(self, s, t):
        dictionary = {}
        for c in s:
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1
        for c in t:
            if c not in dictionary:
                return False
            else:
                if dictionary[c] == 0:
                    return False
                else:
                    dictionary[c] -= 1
        for key in dictionary:
            if dictionary[key] != 0:
                return False
        return True
        

s = "rat"
t = "car"
sol = Solution()
answer = sol.isAnagram(s,t)
print(answer)