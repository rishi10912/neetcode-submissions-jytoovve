from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def solve(i):
            if i <0:
                return 0
            return max(solve(i-1), nums[i]+solve(i-2))
        return solve(n-1)