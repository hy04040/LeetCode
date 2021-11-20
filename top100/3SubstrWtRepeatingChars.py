class Solution(object):
    def lengthOfLongestSubstring(self, s):
        table = {}
        max_count = curr = strt_idx = 0;
        for idx, val in enumerate(s):
            if val in table:
                strt_idx = max(table[val]+1,strt_idx)
                curr = idx - strt_idx + 1
                table[val] = idx
            else:
                curr += 1
                table[val] = idx
            if max_count < curr:
                max_count = curr
        return max_count
        
        
s = ""
sol = Solution()
print(sol.lengthOfLongestSubstring(s))