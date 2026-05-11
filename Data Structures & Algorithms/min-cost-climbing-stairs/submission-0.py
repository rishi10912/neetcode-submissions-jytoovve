class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Edge Case 1
        if n ==1:
            return cost[0]
        #Edge Case 2
        if n==2:
            return min(cost[0],cost[1])
        #Sliding window
        dp0,dp1 = cost[0],cost[1]
        for i in range(2,n):
            current = cost[i] + min(dp0,dp1)
            #Move window forward
            dp0,dp1 = dp1,current
        return min(dp0,dp1)

        