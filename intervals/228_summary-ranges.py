from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        lowerBound = 0
        while i < len(nums):
            lowerBound = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1

            s = str(lowerBound)
            if lowerBound != nums[i]:
                s += "->" + str(nums[i])
                
            res += [s]
            i += 1
        return res