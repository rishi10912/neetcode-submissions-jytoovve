class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
        if len(s) ==0: return True

        my_stack = []

        for char in s:
            if char in my_dict:
                my_stack.append(char)
            else:
                pop_element = my_stack.pop() if my_stack else None
                correct_bracket = my_dict.get(pop_element)
                if char != correct_bracket:
                    return False 
        
        if len(my_stack) !=0 : return False
        return True
