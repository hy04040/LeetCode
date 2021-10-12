
from typing import List
import math
class Solution(object):
    def reverseString(self, s):
        for i in range(0,len(s)//2):
        	s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
        

sol = Solution()
answer = sol.reverseString(["h","e","l","l","o"])
print(answer)
