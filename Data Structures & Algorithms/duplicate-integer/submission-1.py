class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_array =[]
        for i,num in enumerate(nums):
            if num in empty_array:
                return True
            empty_array.append(num)
        return False 