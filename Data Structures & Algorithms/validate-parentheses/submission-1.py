class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        my_stack = []
        if len(s) ==0:
            return True
        for char in s:
            if char in my_dict:
                my_stack.append(char)
            else:
                if my_stack:
                    popped_element = my_stack.pop()
                    correct_bracket = my_dict.get(popped_element)
                    if char != correct_bracket:
                        return False
                else:
                    return False
        if my_stack:
            return False
        return True
