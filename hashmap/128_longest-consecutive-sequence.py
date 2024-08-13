from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxLen = 0
        for num in uniqueNums:
            if num-1 not in uniqueNums:
                curVal = num + 1
                while curVal in uniqueNums:
                    curVal += 1
                if maxLen < curVal - num:
                    maxLen = curVal - num
        return maxLen
