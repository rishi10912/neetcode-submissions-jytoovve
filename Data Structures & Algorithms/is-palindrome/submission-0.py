class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= s.replace('_','')
        s=re.sub(r'\W+', '',s)
        reverse_s = s[::-1]
        if s == reverse_s:
            return True 
        
        else:
            return False
        