from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        # pointers
        cur = 0
        next = 1

        # duplicate tracking
        lastAdded = nums[cur]
        addAgain = True

        while next < len(nums):
            if nums[cur] < nums[next] or addAgain:
                cur += 1
                nums[cur] = nums[next]
                if lastAdded == nums[next]:
                    addAgain = False
                else:
                    lastAdded = nums[cur]
                    addAgain = True
            next += 1
        return cur + 1