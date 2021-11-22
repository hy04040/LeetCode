class Solution:
    def generateParenthesis(self, n):

        if n == 1:
            return {"()"}
        ans = set()
        paren = self.generateParenthesis(n-1)
        for p in paren:
            for i in range(0, len(p)+1):
                for j in range(i, len(p)+1):
                    new_paren = p[:i] + "(" + p[i:j] + ")" + p[j:]
                    ans.add(new_paren)
        return ans 


n = 3
sol = Solution()
print(sol.generateParenthesis(n))

class Solution:
    def generateParenthesis(self, n):
        output=[]
        
        def dfs(index, l_count, r_count, prefix):
            print(index, l_count, r_count, prefix)
            if index==2*n: output.append(prefix)
            
            if l_count>0:
                dfs(index+1,l_count-1,r_count,prefix+'(')
            if r_count>l_count:
                dfs(index+1,l_count,r_count-1,prefix+')')
        
        dfs(0,n,n,'')
        
        return output


class Solution:
    def generateParenthesis(self, n):
        ans = []
        s = ""
        for i in range(n):
            s += "()"
        ans.append(s)
        idx = 0
        while idx != len(ans):
            string = ans[idx]
            right = left = 0
            for i in range(len(string)):
                if string[i] == "(":
                    left += 1
                else:
                    right += 1
                if left == right:
                    for j in range(i+1, len(string)):
                        new_str = string[i+1:j+1]+ string[:i+1] + string[j+1:]
                        if new_str not in ans:
                            ans.append(new_str)
            idx += 1
        return ans


