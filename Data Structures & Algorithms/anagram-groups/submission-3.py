from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            #Frequency Map
            count = [0]*26
            for c in word:
                count[ord('a')-ord(c)] +=1
            # add words to freq map
            result[tuple(count)].append(word)
        return list(result.values())
