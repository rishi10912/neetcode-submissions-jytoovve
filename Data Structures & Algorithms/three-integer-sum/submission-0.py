class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() #sort in ascending order
        for i, num in enumerate(nums):
            if num >0: # No need to iterate past +ve values
                break
            # check for duplicates i encounters
            if i >0 and num == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                totalSum = nums[i] + nums[left] +nums[right]
                if totalSum < 0:
                    left+=1
                elif totalSum > 0:
                    right -=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    # Check for duplicates encountered by left,right
                    while nums[left] == nums[left-1] and left <right:
                        left+=1
        return result
            
            