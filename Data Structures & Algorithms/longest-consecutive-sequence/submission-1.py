class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0 # If empty array
        for num in my_set:
            if (num-1) not in my_set: # Potebtail start of sequence
                length =1 # Array has at least 1 element
                while (num+length) in my_set:
                    length +=1
                longest = max(length,longest)
        return longest
                
        