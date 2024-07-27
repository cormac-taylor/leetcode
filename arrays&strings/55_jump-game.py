from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]
        cur = 0
        end = len(nums) - 1
        
        while cur <= maxJump:
            if maxJump >= end:
                return True
            maxJump = max(maxJump, nums[cur] + cur)
            cur += 1
        return False