class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # creat dict of last seen index
        seen = {} # last index for a given char
        result = []
        for i,char in enumerate(s):
            seen[char] = i
        size = 0 # current size of a given substring
        end = 0 # last seen value of a given char
        for i,char in enumerate(s):
            end = max(end,seen[char])
            size +=1
            if i == end:
                result.append(size)
                size = 0
        return result


        