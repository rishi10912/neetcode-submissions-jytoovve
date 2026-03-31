class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        result = 0 # total water held = min(maxL,maxR) - current_height
        left = 0
        right = len(height)-1

        while left < right:
            if height[left] <= height[right]:
                if height[left] > maxL:
                    maxL = height[left]
                else:
                    current_water = maxL - height[left]
                    result +=current_water
                left +=1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    current_water = maxR-height[right]
                    result +=current_water
                right -=1
        return result

        