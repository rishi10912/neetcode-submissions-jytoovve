# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(0,left)
            right = max(0,right)
            max_sum = max(max_sum,left + right + root.val)
            return root.val + max(left,right)
        dfs(root)
        return max_sum