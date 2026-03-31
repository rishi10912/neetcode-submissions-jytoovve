class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1,max(piles) # Range of rate k
        while left < right:
            # mid point value of k= [1,2,3,4...max(piles)] 
            k = (left+right)//2 # round down
            # Calculate total time for a given k
            total_time =0
            for p in piles:
                total_time += math.ceil(p/k)
            if total_time <=h:
                right = k 
            else:
                left = k+1
        return left

        