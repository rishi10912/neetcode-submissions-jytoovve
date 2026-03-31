class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0 # max area = min(heights[left],heights[right])*(right-left)
        left = 0
        right = len(heights)-1
        while left < right:
            area = min(heights[left],heights[right])*(right-left)
            result = max(result,area)
            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        return result


        