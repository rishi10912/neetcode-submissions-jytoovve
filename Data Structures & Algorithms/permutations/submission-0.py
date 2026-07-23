class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        #DFS backtrack
        def backtrack(start):
            # Base cases 
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start,len(nums)):
                nums[start], nums[i] = nums[i],nums[start]
                backtrack(start+1)
                nums[i],nums[start] = nums[start], nums[i]
        backtrack(0)
        return result
            