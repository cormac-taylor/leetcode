from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        left, right, total = 0, 0, 0
        minWindow = float('inf')
        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target:
                minWindow = min(minWindow, right - left)
                total -= nums[left]
                left += 1
        return minWindow
