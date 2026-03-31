class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left =i
            right = i+1
            while left >= 0 and (heights[left] >= heights[i]):
                left -=1
            while right <len(heights) and (heights[right] >= heights[i]):
                right +=1
            right -=1
            left +=1
            current_area = heights[i]*(right-left+1)
            max_area = max(max_area,current_area)
        return max_area

        