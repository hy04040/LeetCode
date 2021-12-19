from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def dfs(node, depth):
            nonlocal maxD
            if not node:
                if maxD < depth:
                    maxD = depth
                return
            depth += 1
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return maxD
        
        
root = []
n4 = TreeNode(15,None,None)
n5 = TreeNode(7,None,None)
n3 = TreeNode(20,n4,n5)
n2 = TreeNode(9,None,None)
n1 = TreeNode(3,n2,n3)
sol = Solution()
print(sol.maxDepth(n1))

