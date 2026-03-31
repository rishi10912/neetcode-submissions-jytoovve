class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Right sorted portion < left sorted portion
        left,right =0,len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                # mid in the left sorted portion, min is right of mid
                left = mid+1
            else:
                # mid in right sorted portion so mid could be min or left of mid
                right = mid
        return nums[left]
        