class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for char in tokens:
            if char =="+":
                my_stack.append(my_stack.pop()+my_stack.pop())
            elif char =="*":
                my_stack.append(my_stack.pop()*my_stack.pop())
            elif char =="-":
                right = my_stack.pop()
                left = my_stack.pop()
                my_stack.append(left-right)
            elif char =="/":
                right = my_stack.pop()
                left = my_stack.pop()
                my_stack.append(int(left/right))
            else:
                my_stack.append(int(char))
        return my_stack[0]
        