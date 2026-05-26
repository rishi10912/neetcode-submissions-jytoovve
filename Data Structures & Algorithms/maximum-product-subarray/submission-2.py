class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Edge case: Only 1 element
        result = nums[0]
        currMin,currMax =1,1

        for n in nums:
            temp= n*currMax
            currMax = max(n*currMax,n*currMin,n)
            currMin = min(temp,n*currMin,n)
            result = max(result,currMax)
        return result

        