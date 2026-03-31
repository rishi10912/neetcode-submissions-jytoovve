class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        longest = 0
        char_dict = {}
        for right,char in enumerate(s):
            if char in char_dict and char_dict[char] >= left:
                left = char_dict[char] +1
            char_dict[char] = right
            longest = max(longest,right-left+1)
        return longest
        