from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums) # freq Map
        #custome sort
        nums.sort(key=lambda x: (count[x],-x))
        return nums