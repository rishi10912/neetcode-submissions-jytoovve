class Solution(object):
    def create_dict(self,s):
        dict_s = {}
        for char in s:
            if char in dict_s:
                dict_s[char] +=1
            else:
                dict_s[char] =1
        return dict_s

    def isAnagram(self, s, t):
        new_s = self.create_dict(s)
        new_t = self.create_dict(t)
        if new_s == new_t:
            return True
        return False
        