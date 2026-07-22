class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start,path,curr_sum):
            # Base Case
            if curr_sum == target:
                result.append(path.copy())
                return
            for i in range(start,len(candidates)):
                num = candidates[i]
                if i >start and num == candidates[i-1]:
                    continue
                # Purne
                if curr_sum + num > target:
                    break
                path.append(num)
                # recurse
                backtrack(i+1,path,curr_sum+num)
                path.pop()
        backtrack(0,[],0)
        return result


        