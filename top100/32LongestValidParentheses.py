class Solution:
    def longestValidParentheses(self, s: str) -> int:
        S = [-1]
        longest = curr = 0
        for idx in range(0, len(s)):
            if s[idx] == "(":
                S.append(idx)
            else:
                S.pop()
                if len(S) == 0:
                    S.append(idx)
                else:
                    longest = max(longest, idx - S[-1])

        return longest

s = "()(())"
sol = Solution()
print(sol.longestValidParentheses(s))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for i in range(0,n)]
        if s[:2] == "()":
            dp[1] = 2
        for idx in range(2,n):
            if s[idx] == ")":
                if s[idx-1] == "(":
                    dp[idx] = dp[idx-2] + 2
                else:
                    if -1<idx - dp[idx-1]-1 and s[idx - dp[idx-1]-1] == "(":
                        dp[idx] = dp[idx-1]+2
                        if -1 < idx - dp[idx-1]-2:
                            dp[idx] += dp[idx - dp[idx-1]-2]
        return max(dp)