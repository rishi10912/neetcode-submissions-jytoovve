class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            # No triples beyond this as nums is sorted
            if num>0:
                break
            # Duplicate?
            if i>0 and nums[i] ==nums[i-1]:
                continue 
            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = nums[i] + nums[left]+nums[right]
                if threeSum < 0:
                    left +=1
                elif threeSum > 0:
                    right -=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    # skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
        return result

        