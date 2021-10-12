
from typing import List
import math
class Solution(object):
    def reverseWords(self, s):
        ans = ""
        words = s.split()
        for word in words:
            new_word = ""
            for c in reversed(word):
                new_word += c
            ans += new_word + " "
        return ans[:len(ans)-1]

        
        

sol = Solution()
answer = sol.reverseWords("Let's take LeetCode contest")
print(answer)
