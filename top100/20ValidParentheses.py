class Solution(object):
    def isValid(self, s):
        S = []
        left = ["(","{","["]
        right = [')','}',']']
        for c in s:
            if c in left:
                S.append(c)
            else:
                if len(S) == 0:
                    return False
                p = S.pop(-1)
                if left[right.index(c)] != p:
                    return False
        return len(S) == 0





s = "{[}"
sol = Solution()
print(sol.isValid(s))

