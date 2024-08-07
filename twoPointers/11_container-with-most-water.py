from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVolume = 0 
        
        while left < right:
            maxVolume = max(maxVolume, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxVolume