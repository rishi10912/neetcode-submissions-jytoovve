class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Base Case
        if n ==1:
            return nums[0]
        def solve(arr):
            rob1,rob2 = 0,0
            # [rob1,rob2,n,n+1]
            for n in arr:
                temp = max(rob1+n,rob2)
                #Shift window forward
                rob1 = rob2
                rob2= temp 
            return rob2
            
        return max(solve(nums[:-1]),solve(nums[1:]))
        