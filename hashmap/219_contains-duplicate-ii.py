from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexOfLastDup = {}
        for i in range(len(nums)):
            if nums[i] in indexOfLastDup and i - indexOfLastDup[nums[i]] <= k:
                return True
            else:
                indexOfLastDup[nums[i]] = i
        return False