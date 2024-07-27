class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        next = 1

        while next < len(nums):
            if nums[cur] < nums[next]:
                cur += 1
                nums[cur] = nums[next]
            next += 1
        return cur + 1