class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # odd total cannot be split
        if sum(nums) %2:
            return False
        target = sum(nums) //2 
        possible = {0} #Possible sums 
        for num in nums:
            new_sums = set()
            for s in possible:
                new_sums.add(s+num)
                new_sums.add(s)
            possible = new_sums
            if target in possible:
                return True
        return False
