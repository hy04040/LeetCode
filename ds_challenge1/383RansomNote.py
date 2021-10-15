from typing import List

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dictionary = {}
        for c in magazine:
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1

        for note in ransomNote:
            if note in dictionary:
                if dictionary[note] == 0:
                    return False
                else:
                    dictionary[note] -= 1
            else:
                return False
        return True
        

        
        
    

ransomNote = "aa"
magazine = "aab"
sol = Solution()
answer = sol.canConstruct(ransomNote, magazine)
print(answer)