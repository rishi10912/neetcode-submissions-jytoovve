from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree has n-1 edges
        if len(edges) != n-1:
            return False
        # Build Adjacency list
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Visit nodes to see if all nodes connected
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        # Call dfs
        dfs(0)
        # return if all nodes visited
        return len(visited) == n 
        