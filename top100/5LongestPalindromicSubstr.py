class Solution(object):
    def longestPalindrome(self, s):
        def findPalindrome(p, n, start, end):
            curr_start, curr_end = start, end
            curr_s = curr_e = p
            while curr_e < n-1:
                if s[curr_e] == s[curr_e+1]:
                    curr_e += 1
                else:
                    break
            while 0< curr_s and curr_e < n-1:
                if s[curr_s-1] == s[curr_e+1]:
                    curr_s -= 1
                    curr_e += 1
                else:
                    break
            if curr_end - curr_start < curr_e - curr_s:
                curr_start, curr_end = curr_s, curr_e
            return (curr_start, curr_end)
        n = len(s)
        start = end = 0
        if n < 2:
            return s[0]
        for i in range(0, n):
            if (end - start +1) // 2 < n - i:
                (start, end) = findPalindrome(i, n, start, end)
        return s[start:end+1]
        
        
s = "ac"
sol = Solution()
print(sol.longestPalindrome(s))



class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0]*n for i in range(n)]
        longest = 1
        x = y = 0
        for i in range(n):
            dp[i][i] = 1
            if i != n-1 and s[i] == s[i+1]:
                dp[i][i+1] = 2
                if longest == 1:
                    longest = 2
                    x, y = i, i+1
        for l in range(3,len(s)+1):
            for i in range(0, len(s)-l+1):
                j = i+l-1
                if s[i] == s[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if longest < dp[i][j]:
                        longest = dp[i][j]
                        x, y = i, j

        return s[x:y+1]