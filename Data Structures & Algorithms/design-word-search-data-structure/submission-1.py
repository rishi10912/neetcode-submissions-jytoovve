class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]= TrieNode()
            node = node.children[char]
        node.isWord = True
    def search(self, word: str) -> bool:
        def dfs(j,root):
            node = root
            for i in range(j,len(word)):
                # Recursive Backtrack
                if word[i] == ".":
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.isWord
    
        return dfs(0,self.root)
        
