from typing import List

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dictionary = {}
        num = []
        for i in range(0,len(s)):
            dictionary = {}
            for c in s[i:]:
                if c in dictionary:
                    num.append(len(dictionary))
                    break
                else:
                    dictionary[c] = 1
            if len(num) < i+1:
                num.append(len(dictionary))
        if len(num) == 0:
            num.append(0)
        return max(num)

        
        

s = ""
sol = Solution()
answer = sol.lengthOfLongestSubstring(s)
print(answer)