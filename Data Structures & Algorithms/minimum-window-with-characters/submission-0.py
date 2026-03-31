class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t is invalid
        if t == "" or len(t) >len(s): return ""
        char_freq_t = collections.Counter(t)
        char_freq_s = {}
        need = len(char_freq_t)
        have = 0
        result = [-1,-1]
        length = float("inf")
        left = 0

        for right in range(len(s)):
            char_freq_s[s[right]] = char_freq_s.get(s[right],0) +1

            #Update have 
            if s[right] in char_freq_t and char_freq_s[s[right]] == char_freq_t[s[right]]:
                have +=1

            while have == need:
                # Update result 
                if (right - left +1) < length:
                    result = [left,right]
                    length = (right-left+1)
                # Now pop from left 
                char_freq_s[s[left]] -=1
                # update have if target char removed
                if s[left] in char_freq_t and char_freq_s[s[left]] < char_freq_t[s[left]]:
                    have -=1
                left +=1
        p1,p2 = result
        return s[p1:p2+1] if length != float('inf') else ""




        