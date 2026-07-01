class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles) #answer space

        while left < right: # you need min rate
            rate = (left+right)//2
            time =0
            for p in piles:
                time += math.ceil(p/rate)
            if time <=h:
                # decrease to find min rate, could eat slower
                right = rate
            else: # rate too low
                left = rate+1
        return left
             
        