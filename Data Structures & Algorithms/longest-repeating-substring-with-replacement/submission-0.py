class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            # Count occurence of each char
            char_freq[s[right]] = char_freq.get(s[right],0) +1
            while (right - left + 1) - max(char_freq.values()) > k:
                char_freq[s[left]] -=1
                left +=1
            longest = max(longest, right - left + 1)
        return longest