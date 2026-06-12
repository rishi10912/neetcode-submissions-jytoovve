class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Build adjacency list
        adj = {c:set() for w in words for c in w}

        #check order
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            # edge case where prefix comes after the word
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    #Build connections
                    adj[w1[j]].add(w2[j])
                    break 
        #Traversal of nodes
        visited ={}
        result = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True

            for nei in adj[char]:
                #Cycle ?
                if dfs(nei):
                    return True
            visited[char] = False
            result.append(char)
        for c in adj:
            #Cycle Detected
            if dfs(c):
                return "" 
        result.reverse()
        return "".join(result)
        
            
        