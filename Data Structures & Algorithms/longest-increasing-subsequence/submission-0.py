class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Longest Increasing Subsequence starting at index i
        LIS = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] <nums[j]:
                    # What if I connect nums[i] to the subsequence starting at j?
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)
        