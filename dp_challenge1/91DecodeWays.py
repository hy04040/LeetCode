class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0]*n
        if s[0] == '0':
            dp[0] = 0
        else:
            dp[0] = 1
        for i in range(1,n):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] =='2':
                    if i<2:
                        dp[i] = 1
                    else:
                        dp[i] = dp[i-2]
                else:
                    return 0
            elif 10 < int(s[i-1:i+1]) and int(s[i-1:i+1])<27:
                if i < 2:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]

        


        

s = "06"
sol = Solution()
print(sol.numDecodings(s))