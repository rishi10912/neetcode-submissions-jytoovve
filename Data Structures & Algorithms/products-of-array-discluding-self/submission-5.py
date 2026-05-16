class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product =1
        zero_count = 0
        for num in nums:
            if num:
                product *=num
            else:
                zero_count +=1
        # Check if more than 1 zero
        if zero_count > 1:
            return [0]*n
        # If only 1 zero or no zero
        result = [0]*n
        for i,c in enumerate(nums):
            if zero_count:
                if c == 0:
                    result[i] = product
                else:
                    result[i] = 0
            else:
                result[i] = product//c
        return result
        