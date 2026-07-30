class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        # helper function
        def is_palindrome(string):
            return string == string[::-1]
        
        def backtrack(start,path):
            # base case
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start+1,len(s)+1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end,path)
                    path.pop()
                
        backtrack(0,[])
        return result