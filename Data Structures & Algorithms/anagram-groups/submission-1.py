class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            freq_map = [0]*26
            for char in s:
                freq_map[ord(char)-ord('a')] +=1
            result[tuple(freq_map)].append(s)
        return list(result.values())


        