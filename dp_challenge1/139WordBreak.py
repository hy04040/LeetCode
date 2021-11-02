class Solution(object):
    def wordBreak(self, s, wordDict):
        dictionary = {}
        length = len(s)
        dp = [False]*length
        for word in wordDict:
        	dictionary[word] = True
        search = ""
        found = ""
        dp[0] = s[0] in dictionary
        for i in range(1, length):
        	for j in range(0, i+1):
        		if j != i:
	        		if dp[j] and s[j+1:i+1] in dictionary:
	        			dp[i] = True
	        			break
        		else:
        			if s[:i+1] in dictionary:
        				dp[i] = True
        return dp[length-1]
        

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
sol = Solution()
print(sol.wordBreak(s, wordDict))