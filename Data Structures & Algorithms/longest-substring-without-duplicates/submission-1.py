class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        char_set = set()
        longest = 0
        for right in range(len(s)):
            current_char = s[right]
            while current_char in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(current_char)
            longest = max(longest,right-left +1)
        return longest

        