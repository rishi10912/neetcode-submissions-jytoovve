class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        #Edge case nums is NONE
        longest = 0
        for num in my_set:
            # start of potential squence
            if num-1 not in my_set:
                length =1
                while num+length in my_set:
                    length +=1
                longest = max(longest,length)       
        return longest
        