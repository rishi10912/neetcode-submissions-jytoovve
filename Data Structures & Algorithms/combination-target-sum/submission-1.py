class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(start,path,curr_sum):
            # Base Case
            if curr_sum == target:
                result.append(path.copy())
                return
            for i in range(start,len(nums)):
                num = nums[i]
                # Purne
                if curr_sum + num > target:
                    break
                path.append(num)
                # recurse
                backtrack(i,path,curr_sum+num)
                path.pop()
        backtrack(0,[],0)
        return result
