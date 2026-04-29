class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        #DFS backtrack
        def backtrack(start,path,curr_sum):
            # Base cases 
            if curr_sum == target:
                result.append(path.copy())
                return
            for i in range(start,len(nums)):
                num = nums[i]
                # Prune 
                if curr_sum + num > target:
                    break
                path.append(num)
                backtrack(i,path,curr_sum+num)
                path.pop()
        backtrack(0,[],0)
        return result
        
        