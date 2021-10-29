class Solution(object):
    def getMaxLen(self, nums):
        n = len(nums)
        longest = pos = neg = 0
        if nums[0] < 0:
            neg = 1
        elif nums[0] > 0:
            pos = 1
            longest= 1
        for i in range(1, n):
            if nums[i] == 0:
                pos = 0
                neg = 0
            elif nums[i] > 0:
                if neg == 0:
                    neg = 0
                else:
                    neg = neg+1
                pos += 1
            else:
                temp = pos
                if neg == 0:
                    pos = 0
                else:
                    pos = neg + 1
                neg = temp + 1
            if longest < pos:
                    longest = pos
        return longest
        

        


sol = Solution()
nums = [1,2,3,5,-6,4,0,10]
nums = [-7,-10,-7,21,20,-12,-34,26,2]
nums = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
answer = sol.getMaxLen(nums)
print(answer)