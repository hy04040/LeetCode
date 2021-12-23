from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(node):
            nonlocal ans
            left_val = right_val = float("-inf")
            if not (node.left or node.right):
                return node.val
            if node.left:
                left_val = dfs(node.left)
            if node.right:
                right_val = dfs(node.right)
            ans = max(ans, left_val+node.val+right_val, left_val+node.val, right_val+node.val, node.val, left_val, right_val)
            return max(left_val+node.val, node.val+right_val, node.val)
        dfs(root)
        return ans



       
t5 = TreeNode(7, None, None)
t4 = TreeNode(15, None, None)
t3 = TreeNode(20, t4, t5)
t2 = TreeNode(9, None, None) 
root = TreeNode(-10, t2, t3)

t7 = TreeNode(-1, None, None)
t6 = TreeNode(-2, None, None)
t5 = TreeNode(3, None, None)
t4 = TreeNode(1, t7, None)
t3 = TreeNode(-3, t6, None)
t2 = TreeNode(-2, t4, t5) 
root = TreeNode(1, t2, t3)

sol = Solution()
print(sol.maxPathSum(root))

