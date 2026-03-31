class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        right = 0 #sell
        left = 0 # buy

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                result = max(result,profit)
            else:
                left = right
            right +=1
        return result

        