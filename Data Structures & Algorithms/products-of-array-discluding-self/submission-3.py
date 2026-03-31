class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        result = [1]*n
        
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix =1 

        for j in range(n-1,-1,-1):
            result[j] *= suffix
            suffix *= nums[j]
        return result
        

        