from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Initial check 
        if len(edges) != n-1:
            return False
        # build adjacency list
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        #Cycle detection in undirected graph
        def dfs(node,parent):
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue #avoids false positive
                if nei in visited or dfs(nei,node):
                    return True
            return False
        if dfs(0,None):
            return False
        # Check for unconnected nodes
        return len(visited) == n

