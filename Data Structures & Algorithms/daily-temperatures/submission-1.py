class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        my_stack = [] # stores index
        for i in range(n):
            while my_stack and temperatures[i] > temperatures[my_stack[-1]]:
                prevIndex = my_stack.pop()
                result[prevIndex] = i - prevIndex
            my_stack.append(i)
        return result
        