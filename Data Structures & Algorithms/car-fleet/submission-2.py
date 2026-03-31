class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position,speed))
        my_stack = [] # monotonic increasing time

        for p,s in sorted(pair,reverse = True):
            time = (target-p)/s
            my_stack.append(time)
            if len(my_stack)>=2 and my_stack[-1] <= my_stack[-2]:
                my_stack.pop()
        return len(my_stack)
        