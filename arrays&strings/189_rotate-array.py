from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        temp = 0
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1