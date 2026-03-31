# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def dfs_inOrder(root):
            if not root:
                return
            dfs_inOrder(root.left)
            result.append(root.val)
            dfs_inOrder(root.right)
        dfs_inOrder(root)
        return result[k-1]
        