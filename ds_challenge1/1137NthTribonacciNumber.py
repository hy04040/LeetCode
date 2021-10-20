from typing import List

class Solution(object):
    def tribonacci(self, n):
        fib = []
        fib.append(0)
        fib.append(1)
        fib.append(1)
        for i in range(3,n+1):
            fib.append(fib[i-1]+fib[i-2]+fib[i-3])
        return fib[n]
        

sol = Solution()
answer = sol.tribonacci(25)
print(answer)