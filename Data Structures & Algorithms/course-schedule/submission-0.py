from collections import defaultdict, deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build Adjacency list and Indegree array
        n = numCourses
        indegree = [0] *n
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        # Implement topo sort 
        q = deque()
        for i in range(n):
            if indegree[i] ==0:
                q.append(i)
        count =0        
        while q:
            node = q.popleft()
            count +=1
            #explore neighbors
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] ==0:
                    q.append(nei)
        return count ==n


        