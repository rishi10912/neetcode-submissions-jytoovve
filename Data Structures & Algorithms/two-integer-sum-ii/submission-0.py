class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,num in enumerate(numbers):
            possibleSolution = target - num
            if possibleSolution in my_dict:
                return[my_dict[possibleSolution]+1,i+1]
            my_dict[num]=i
        