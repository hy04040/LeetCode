from typing import List

class Solution(object):
    def checkInclusion(self, s1, s2):
        dictionary = {}
        for c in s1:
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1
        s1_length = len(s1)
        for idx,c in enumerate(s2[:len(s2)-s1_length+1]):
            if c in dictionary:
                new_dict = {}
                for c2 in s2[idx:idx+s1_length]:
                    if c2 in new_dict:
                        new_dict[c2] += 1
                    else:
                        new_dict[c2] = 1
                if dictionary == new_dict:
                    return True
        return False

s1 = "adc"
s2 = "dcda"
sol = Solution()
answer = sol.checkInclusion(s1,s2)
print(answer)