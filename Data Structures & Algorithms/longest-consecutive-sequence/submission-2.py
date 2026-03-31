class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0 # When nums is NONE

        for num in nums_set:
            if num-1 not in nums_set: #start of a potential sequence 
                length = 1 # at least 1 element present 
                while num + length in nums_set:
                    length+=1
                longest = max(longest,length)
        return longest 
            
        