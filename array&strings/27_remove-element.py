class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        leftPtr = 0
        rightPtr = len(nums) - 1

        while leftPtr <= rightPtr:
            if nums[leftPtr] == val:
                nums[leftPtr] = nums[rightPtr]
                rightPtr -= 1
            else:
                leftPtr += 1
        return leftPtr