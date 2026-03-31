# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # build dict of {val:i}
        my_dict = {val:i for i, val in enumerate(inorder)}
        root_index = 0

        def dfs(left,right): # left and rirght are indices in inorder 
            nonlocal root_index
            if left > right: #prevents the call dfs(0,-1)
                return
            # get root index
            root_val = preorder[root_index]
            # confusion here nut this hsould be done before recursive call
            root_index +=1
            
            root = TreeNode(root_val)
            mid = my_dict[root_val]
            #build left and right subtree
            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)
            return root
        
        
        return dfs(0,len(inorder)-1)