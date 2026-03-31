class Solution:
    def isValid(self, s: str) -> bool:
        my_hashmap = {
        "}" : "{",
        ")" : "(",
        "]" : "[",
        }
        stack = []
        
        for char in s:
            if char in my_hashmap: #for closing bracket
                popped_element = stack.pop() if stack else None
                if my_hashmap[char] != popped_element:
                    return False
            else: #for opening bracket
                stack.append(char)
        return not stack #returns true if stack is empty

        