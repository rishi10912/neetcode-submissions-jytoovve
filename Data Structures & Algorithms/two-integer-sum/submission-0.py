class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i,num in enumerate(nums):
            possibleSolution = target - num
            if possibleSolution in dict:
                return [dict[possibleSolution], i]
            dict[num] = i