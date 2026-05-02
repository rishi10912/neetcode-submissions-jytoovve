"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # seen nodes
        oldToNew = {}
        def dfs_clone(node):
            #Base Case, Clone already exists 
            if node in oldToNew:
                return oldToNew[node]
            # create copy
            copy = Node(node.val)
            #Update seen
            oldToNew[node] = copy
            #explore neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei))
            return copy
        return dfs_clone(node) if node else None

            
        