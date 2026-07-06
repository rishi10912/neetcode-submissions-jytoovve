class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        total = len(a)+ len(b)
        half = total//2 # ~left half should contain these many elements
        if len(a)>len(b):
            a,b =b,a
        left,right = 0, len(a)

        while True:
            i = (left+right)//2
            j = half-i
            AL = a[i-1] if i >0 else float("-inf")
            AR = a[i] if i<len(a) else float("inf")
            BL = b[j-1] if j >0 else float("-inf")
            BR = b[j] if j<len(b) else float("inf")

            if AL <= BR and BL<=AR:
                if total%2:
                    return min(AR,BR)
                return (max(AL,BL)+min(AR,BR))/2
            elif AL>BR:
                right = i-1
            else:
                left = i+1
        