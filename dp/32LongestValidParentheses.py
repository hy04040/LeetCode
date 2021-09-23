from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = []
        max_count = 0;
        dp.append(0)
        for i in range(1,len(s)):
            dp.append(0)
            if s[i] == ")":
                if dp[i-1] != 0:
                    if (0 < i-dp[i-1]) and (s[i-dp[i-1]-1] == "("):
                        dp[i] = dp[i-1] + 2
                elif s[i-1] == "(":
                    dp[i] = 2
                    if (-1<i-2):
                        dp[i] += dp[i-2]
            if -1<i-dp[i]:
                dp[i] += dp[i-dp[i]]
            max_count = max(max_count, dp[i])
        return max_count
        
sol = Solution()
fp = open("input.txt", "r")
string = fp.readlines()[0]
answer = sol.longestValidParentheses(string)
print(answer)