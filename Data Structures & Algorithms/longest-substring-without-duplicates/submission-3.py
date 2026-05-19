class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right =0
        seen = set()
        longest = 0 # Result
        for right in range(len(s)):
            current = s[right]
            # Move left pointer until repeat gone
            while current in seen:
                seen.remove(s[left])
                left +=1
            seen.add(current)
            longest = max(longest,right-left+1)
        return longest