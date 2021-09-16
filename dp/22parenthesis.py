class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def findParenthesis(string):
            left = 0;
            right = 0
            parenthesis = ""
            for s in string:
                parenthesis += s
                if s == "(":
                    left += 1
                else:
                    right += 1
                if left == right:
                    return parenthesis
        def generate(ans, paren, string):
            for i in range(len(string)):
                gen = string[:i] + paren + string[i:]
                if gen not in ans:
                    ans.append(gen)
        def solve(ans, original, n):
            new = len(ans)
            if len(ans) is 0:
                ans.append("()")
                return
            for a in ans[len(ans)-n:]:
                paren = findParenthesis(a)
                generate(ans, paren, a[len(paren):])
            new = len(ans) - new
            if new is 0:
                return
            else:
                solve(ans, original, new)

        T = n
        ans = []
        original = ""
        for x in range(n):
            original += "()"
        paren = findParenthesis(original)
        generate(ans, paren, original[len(paren):])
        solve(ans, original, len(ans))
        return ans