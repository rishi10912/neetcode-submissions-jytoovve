class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left =0

        for right in range(len(s)):
            #char map
            count[s[right]] = count.get(s[right],0)+1
            #if we exceed max number of changes
            while (right-left+1) -max(count.values())>k:
                # decrement frequency of at left as we move left forward
                count[s[left]] -=1
                left+=1
            result = max(result,right-left+1)
        return result
        