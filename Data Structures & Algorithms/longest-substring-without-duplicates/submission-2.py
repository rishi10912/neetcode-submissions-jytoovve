class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_set =set()
        longest = 0 #result 

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(s[right])
            longest = max(longest,right-left+1)
        return longest
        