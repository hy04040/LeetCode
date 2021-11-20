class Solution(object):
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []
        table = dic = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8": ["t","u","v"], "9":["w","x","y","z"]}
        def add_char(digits, idx, result, table):
            if idx == len(digits):
                return result
            key = digits[idx]
            res = []
            if idx == 0:
                res = table[key]
            else:
                for i in range(0, len(result)):
                    for j in range(0, len(table[key])):
                        res.append(result[i]+table[key][j])
            return add_char(digits, idx+1, res, table)
        ans = add_char(digits, 0, [], table)
        return ans


digits = "23"
sol = Solution()
print(sol.letterCombinations(digits))


class Solution(object):
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []
        table = {}
        num = 97
        for i in range(2,10):
            if i == 7 or i == 9:
                table[i] = [chr(num), chr(num+1), chr(num+2), chr(num+3)]
                num += 4
            else:
                table[i] = [chr(num), chr(num+1), chr(num+2)]
                num += 3
        dp = [[] for i in range(n)]
        for idx,val in enumerate(digits):
            if idx == 0:
                dp[0] = table[int(val)]
            else:
                for i in range(0, len(dp[idx-1])):
                    for j in range(0, len(table[int(val)])):
                        dp[idx].append(dp[idx-1][i] + table[int(val)][j])
        return dp[-1]

