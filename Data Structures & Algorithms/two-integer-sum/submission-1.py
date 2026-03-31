class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i,num in enumerate(nums):
            possibleSol = target - num
            if possibleSol in my_dict:
                return[my_dict[possibleSol],i]
            my_dict[num] = i

        return None