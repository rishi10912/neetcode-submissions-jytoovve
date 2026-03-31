class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxL =0
        maxR = 0 
        total_water =0

        while left < right:
            if height[left] < height[right]:
                if height[left] > maxL:
                    maxL = height[left]
                else:
                    current_water = maxL - height[left]
                    total_water += current_water
                left +=1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    current_water = maxR - height[right]
                    total_water += current_water                
                right -=1
        return total_water
        