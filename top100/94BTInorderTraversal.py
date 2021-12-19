from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left, Root, Right
        ans = []
        if not root:
            return []
        ans.extend(self.inorderTraversal(root.left))
        ans.append(root.val)
        ans.extend(self.inorderTraversal(root.right))
        return ans
        
#[3,1,null,null,2]     
n3 = TreeNode(2,None,None)
n2 = TreeNode(1,None,n3)
n1 = TreeNode(3,n2,None)
sol = Solution()
print(sol.inorderTraversal(n1))

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left, Root, Right
        values = []
        def traverse(node):
            if not node:
                return
            nonlocal values
            left = node.left
            traverse(left)
            values.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(root)
        return values