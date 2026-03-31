class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Check if s1 valid
        if len(s1) > len(s2):
            return False
        
        freq_map1 = [0]*26
        for char in s1:
            freq_map1[ord(char)-ord('a')] +=1

        freq_map2 = [0]*26

        for i in range(len(s2)):
            freq_map2[ord(s2[i])-ord('a')] +=1
            '''When the window grows beyond the target size, 
            we decrement the frequency of the character that falls out from the left, 
            which is at index i - len(s1).'''
            if i >= len(s1):
                freq_map2[ord(s2[i-len(s1)])- ord('a')] -=1
            if freq_map1 == freq_map2:
                return True
        return False




        