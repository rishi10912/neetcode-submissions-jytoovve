class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        result = [0]*n
        my_stack = []
        for i in range(n):
            while my_stack and temperatures[i] > temperatures[my_stack[-1]]:
                PrevIndex = my_stack.pop()
                result[PrevIndex] = i - PrevIndex
            my_stack.append(i)
        return result
        